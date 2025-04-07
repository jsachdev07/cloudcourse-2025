#!/bin/bash

# Ensure the script is run with sudo or root privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "This script requires root privileges. Please run as root or with sudo."
    exit 1
fi

# Function to check if the disk is mounted
is_mounted() {
    mount | grep "$1" > /dev/null 2>&1
    return $?
}

# Function to log actions
log_action() {
    echo "$(date) - $1" >> /var/log/disk_setup.log
}

# Step 1: Loop until all disks are mounted
while true; do
    echo "Listing available disks and their sizes (excluding OS disks):"

    # Use lsblk to list all disks, excluding system disks (e.g., /dev/sda, /dev/vda, /dev/nvme, /dev/xvd)
    # Mark the mounted disks in the list
    lsblk -d -o NAME,SIZE | grep -E '^sd|^nvme|^vd|^xvd' | grep -Ev '^(sda|vda|nvme|xvda)' | while read line; do
        # For each disk, prepend /dev/ to the disk name
        DISK_PATH="/dev/$(echo $line | awk '{print $1}')"
        DISK_SIZE=$(echo $line | awk '{print $2}')
       
        # Check if the disk is already mounted
        if is_mounted "$DISK_PATH"; then
            echo "$DISK_PATH - $DISK_SIZE - Already mounted"
        else
            echo "$DISK_PATH - $DISK_SIZE - Not mounted"
        fi
    done

    # Step 2: Ask the user to choose a disk to mount (only if the disk is not mounted)
    read -p "Enter the full disk path to format and mount (or type 'exit' to quit): " DISK

    # Exit the loop if user types 'exit'
    if [ "$DISK" == "exit" ]; then
        echo "Exiting the script."
        break
    fi

    # Validate the disk input
    if [ ! -b "$DISK" ]; then
        echo "Invalid disk: $DISK does not exist."
        continue
    fi

    # Check if the disk is already mounted
    if is_mounted "$DISK"; then
        echo "$DISK is already mounted."
        continue
    fi

    # Step 3: Ask the user to specify the mount path
    read -p "Enter the mount path: " MOUNT_PATH

    # Validate if the mount directory exists, create if it doesn't
    if [ ! -d "$MOUNT_PATH" ]; then
        read -p "Directory $MOUNT_PATH does not exist. Would you like to create it? (y/n): " CREATE_DIR
        if [ "$CREATE_DIR" == "y" ]; then
            mkdir -p "$MOUNT_PATH"
            echo "Directory created: $MOUNT_PATH"
            log_action "Created directory: $MOUNT_PATH"
        else
            echo "Exiting script. Mount directory is required."
            continue
        fi
    fi

    # Check if the mount path is empty
    if [ "$(ls -A $MOUNT_PATH)" ]; then
        echo "Mount path $MOUNT_PATH is not empty. Please provide a different mount point."
        continue
    fi

    # Step 4: Unmount the disk if already mounted
    umount "$DISK" 2>/dev/null

    # Step 5: Confirm before formatting the disk
    read -p "Are you sure you want to format $DISK? This will erase all data on the disk. (y/n): " CONFIRM
    if [ "$CONFIRM" != "y" ]; then
        echo "Skipping disk formatting."
        continue
    fi

    # Step 6: Create the XFS filesystem on the specified disk
    echo "Creating XFS filesystem on $DISK..."
    mkfs.xfs "$DISK" || { echo "Failed to format $DISK"; continue; }

    # Step 7: Mount the disk to the specified mount path
    echo "Mounting $DISK to $MOUNT_PATH..."
    mount "$DISK" "$MOUNT_PATH" || { echo "Failed to mount $DISK"; continue; }

    # Step 8: Verify if the mount was successful
    if mount | grep "$DISK" > /dev/null; then
        echo "Successfully mounted $DISK to $MOUNT_PATH."
        log_action "Successfully mounted $DISK to $MOUNT_PATH"
    else
        echo "Failed to mount $DISK."
        continue
    fi

    # Step 9: Get the UUID of the disk
    UUID=$(blkid -s UUID -o value "$DISK")
    if [ -z "$UUID" ]; then
        echo "Failed to retrieve UUID for $DISK."
        continue
    fi

    # Step 10: Ask user if they want to add the mount to /etc/fstab using UUID
    read -p "Do you want to add this mount to /etc/fstab for persistence using UUID? (y/n): " ADD_FSTAB
    if [ "$ADD_FSTAB" == "y" ]; then
        # Backup the current /etc/fstab before making changes
        cp /etc/fstab /etc/fstab.bak
        echo "Backup of /etc/fstab created as /etc/fstab.bak."

        # Add entry to /etc/fstab using UUID
        echo "UUID=$UUID $MOUNT_PATH xfs defaults 0 2" >> /etc/fstab
        echo "Added UUID=$UUID to /etc/fstab for persistence."
        log_action "Added UUID=$UUID to /etc/fstab"
    fi

    # Check if all disks are now mounted
    all_mounted=true
    lsblk -d -o NAME | grep -E '^sd|^nvme|^vd|^xvd' | grep -Ev '^(sda|vda|nvme|xvda)' | while read line; do
        DISK_PATH="/dev/$(echo $line)"
        if ! is_mounted "$DISK_PATH"; then
            all_mounted=false
            break
        fi
    done

    # If all disks are mounted, exit the loop
    if [ "$all_mounted" == true ]; then
        echo "All disks have been mounted."
        break
    fi
done

echo "Script completed successfully."
