# 🌐 Mount Amazon EFS on Two EC2 Instances Across Different Availability Zones

This guide shows how to mount a shared Amazon EFS file system on **two EC2 instances located in different AZs**, using Amazon Linux.

---

## ✅ Overview

- **EFS** is multi-AZ by design — data is replicated across AZs.
- Mounting EFS on EC2s in **different AZs** provides:
  - High availability
  - Redundancy
  - Better fault tolerance

---

## ✅ Prerequisites

- Two **Amazon Linux EC2 instances** in **different Availability Zones**, within the **same VPC** and **same region**.
- One **Amazon EFS File System** created in the same VPC.
- Proper **security group settings** for NFS (port 2049).

---

## ✅ Step 1: Security Group Configuration

1. Create or edit a **shared security group** that will be attached to both EC2s.
2. Add an **inbound rule**:
   - **Type:** NFS
   - **Protocol:** TCP
   - **Port Range:** 2049
   - **Source:** The **same security group** (i.e., itself)

This allows both instances to communicate with EFS and each other securely.

---

## ✅ Step 2: Launch EC2 Instances in Different AZs

1. Launch **Instance A** in **AZ-1** (e.g., `us-east-1a`)
2. Launch **Instance B** in **AZ-2** (e.g., `us-east-1b`)
3. Attach the **shared security group** to both.
4. Ensure both instances are in the **same VPC**.

---

## ✅ Step 3: Create & Configure EFS

1. Go to **EFS > Create file system**
2. Choose the **same VPC** as your EC2s
3. AWS will automatically create **mount targets in all available AZs** (make sure targets exist for both AZs of your EC2s)
4. Note your **File System ID** (e.g., `fs-abc12345`)

---

## ✅ Step 4: Install EFS Utils on Both EC2s

SSH into **both EC2 instances** and run:

sudo yum install -y amazon-efs-utils

## ✅ Step 5: Mount EFS on Both Instances
On both EC2s, create a mount point:

sudo mkdir /mnt/efs
Mount the EFS:

sudo mount -t efs fs-abc12345:/ /mnt/efs

Replace fs-abc12345 with your actual EFS File System ID.

## ✅ Step 6: Test Shared Access
On Instance A:

cd /mnt/efs
echo "Hello from AZ-1" | sudo tee az1.txt

On Instance B:

cd /mnt/efs
cat az1.txt  # Should display: Hello from AZ-1
🎉 Now both instances are reading/writing to the same file system, across different Availability Zones!

✅ (Optional) Step 7: Auto-Mount on Reboot
Add this line to /etc/fstab on both instances:

fs-abc12345:/ /mnt/efs efs defaults,_netdev 0 0

✅ Done!
You now have:

Two EC2 instances in different AZs

Mounting a shared EFS file system

Ensuring high availability, durability, and failover resilience




