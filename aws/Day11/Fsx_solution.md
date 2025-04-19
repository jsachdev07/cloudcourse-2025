# AWS Windows Server Setup with Active Directory, FSx, and Security Groups

## 🛠️ **Step 1: Create Security Groups for EC2 Instances and FSx**

### 1. **Create Security Group for EC2 Instances (SG-EC2)**:
   - **Name**: `SG-EC2-Windows`
   - **Description**: Security Group for EC2 instances (Windows servers and AD)
   - **VPC**: Select the VPC where your instances will be deployed.

   **Inbound Rules**:
   - **Allow all traffic** from other EC2 instances in the same security group (SG-EC2-Windows) for communication between AD, client servers, and FSx.
   
     Example:
     | Type       | Protocol | Port Range  | Source           |
     |------------|----------|-------------|------------------|
     | All Traffic| All      | All         | 0.0.0.0/0        |

   **Outbound Rules**:
   - Allow all outbound traffic for testing purposes (can be refined later).
   
     Example:
     | Type       | Protocol | Port Range | Destination      |
     |------------|----------|------------|------------------|
     | All Traffic| All      | All        | 0.0.0.0/0        |

---

### 2. **Create Security Group for FSx (SG-FSx)**:
   - **Name**: `SG-FSx`
   - **Description**: Security Group for FSx access control.
   - **VPC**: Same VPC as EC2 instances.

   **Inbound Rules for FSx**:
   - **Allow all inbound traffic** from the **SG-EC2-Windows** security group. This ensures communication between the EC2 instances and FSx.
   
     Example:
     | Type       | Protocol | Port Range  | Source           |
     |------------|----------|-------------|------------------|
     | All Traffic| All      | All         | SG-EC2-Windows   |

   **Outbound Rules**:
   - Allow all outbound traffic for FSx or restrict it if needed.

     Example:
     | Type       | Protocol | Port Range | Destination      |
     |------------|----------|------------|------------------|
     | All Traffic| All      | All        | 0.0.0.0/0        |

---

## 🛠️ **Step 2: Create the Windows EC2 Instances**

1. **Launch EC2 Instances**:
   - **Instance 1 (AD Server)**: Launch a Windows EC2 instance in `us-east-1a` and assign it **SG-EC2-Windows**.
   - **Instance 2 (Client Server 1)**: Launch another Windows EC2 instance in `us-east-1a` and assign it **SG-EC2-Windows**.
   - **Instance 3 (Client Server 2)**: Launch another Windows EC2 instance in `us-east-1b` and assign it **SG-EC2-Windows**.

2. **Ensure RDP Access**:
   - Open **RDP port 3389** for these instances in the **SG-EC2-Windows** security group to allow RDP access.

---

## 🛠️ **Step 3: Configure the AD Server (Active Directory Configuration)**

1. **Connect to AD Server** (`Instance 1` in `us-east-1a`) via RDP:
   - Use **Remote Desktop Protocol (RDP)** to connect to the instance.

2. **Change Admin Password**:
   - Log in as **Administrator** and change the admin password to something secure.

3. **Set Static IP Address**:
   - Open **Control Panel** → **Network and Sharing Center** → **Change adapter settings**.
   - Right-click the network adapter → **Properties** → **Internet Protocol Version 4 (TCP/IPv4)** → **Use the following IP address**.
     - Set a static IP address (e.g., `10.0.1.10` in `us-east-1a` subnet).

4. **Change Hostname**:
   - Open **Control Panel** → **System** → **Change Settings**.
   - Change the computer name to something like `AD-SERVER`.
   - Reboot the instance for changes to take effect.

5. **Install Active Directory Domain Services (AD DS)**:
   - Open **Server Manager** → **Add Roles and Features** → Select **Active Directory Domain Services**.
   - Follow the wizard and install the **AD DS** role.
   - Once installed, click on the **notification flag** and **Promote this server to a domain controller**.

6. **Configure Active Directory (abc.local)**:
   - Set up a **new forest** with the domain name `abc.local`.
   - Set the **Directory Services Restore Mode (DSRM)** password.
   - Complete the wizard and allow the server to restart.

   Once restarted, your **Active Directory** server will be fully set up with domain `abc.local`.

---

## 🛠️ **Step 4: Configure Client1 (Windows Server 2 in us-east-1a)**

1. **Connect to Client1 Server** (`Instance 2` in `us-east-1a`) via RDP.

2. **Set Static IP Address** (if not already done):
   - Same process as you did for the AD server.

3. **Change Hostname**:
   - Go to **Control Panel** → **System** → **Change Settings** → **Change** the hostname to something like `CLIENT1`.
   - Reboot the instance.

4. **Set DNS Server to AD Server**:
   - Open **Control Panel** → **Network and Sharing Center** → **Change adapter settings**.
   - Right-click the network adapter → **Properties** → **Internet Protocol Version 4 (TCP/IPv4)** → **Use the following DNS server addresses**.
     - Set **DNS server** IP to the **static IP** of the **AD Server** (e.g., `10.0.1.10`).

5. **Reboot the instance** after DNS changes.

6. **Client 2 in us-east-1b** Repeat the same steps for windows server in us-east-1b

---

## 🛠️ **Step 5: Join Client1 and Client2 to the Domain**

1. **On Client1 and on Client2**, go to **System Properties** → **Change settings** → **Change**.
2. Choose **Domain** and enter `abc.local` as the domain.
3. Provide **domain credentials** (e.g., `Administrator`).
4. Click **OK** and restart the server to complete the domain join.

Once restarted, **Client1 and Client2** should be part of the `abc.local` domain.

---

## 🛠️ **Step 6: FSx Creation**

- **You will create the FSx for Windows File Server** in the AWS Management Console and configure it with **self-managed Active Directory (AD)** details (which are `abc.local` and AD Server IP `10.0.1.10` in your case).

  **Important Details for FSx Creation**:
  - **Active Directory details**:
    - **Domain Name**: `abc.local`
    - **DNS Servers**: IP of AD Server (e.g., `10.0.1.10`)
    - **Service Account Credentials**: Domain Administrator credentials to join FSx to the domain.
  - **Deployment**: Make sure FSx is deployed in the same **VPC** as your Windows EC2 instances and within the same **subnets (us-east-1a and us-east-1b)** for high availability.

---

## 🛠️ **Step 7: Mount the FSx File System on EC2 Instances**

Once your **FSx file system** is created and ready:

1. **On Client1 (Windows Server us-east-1a)**:
   - Open **Command Prompt** or **PowerShell** as Administrator.
   - Mount the FSx file system:
     ```powershell
     net use Z: \\fs-xxxxxxxx.fsx.us-east-1.amazonaws.com\share-name /user:abc\username
     ```
   - Replace `fs-xxxxxxxx.fsx.us-east-1.amazonaws.com` with the actual FSx DNS name and `share-name` with the share you want to access.

2. **On Client2 (Windows Server in us-east-1b)**:
   - Same as **Client1**, run the **net use** command to mount the FSx share.

   **Note**: You may need to use **domain credentials** to authenticate and access the FSx share.

---

## 📌 **Summary of Steps Completed**
1. **Security Groups**: Created for EC2 and FSx, with inbound traffic allowed from the EC2 security group to FSx (all traffic allowed).
2. **Windows Instances**: Created in `us-east-1a` (AD Server & Client1) and `us-east-1b` (Client2).
3. **AD Server Configuration**: Installed and configured **Active Directory** (`abc.local`).
4. **Client1 Configuration**: Set DNS and joined the domain.
5. **FSx Configuration**: Details provided for connecting FSx to **abc.local** AD.
6. **Mount FSx**: FSx share will be mounted on EC2 instances.

---
