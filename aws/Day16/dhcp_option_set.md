# 📘 AWS DHCP Option Set – Overview, Use Case, and Steps

---

## ✅ What Is a DHCP Option Set in AWS?

A **DHCP Option Set** in AWS allows you to configure how EC2 instances in a VPC receive network settings such as:

- **Domain name**
- **DNS servers**
- **NTP servers** (for time synchronization)
- **NetBIOS name servers** (optional)

By default, AWS provides a DHCP option set with:
- Domain name: `ec2.internal` (or `<region>.compute.internal`)
- DNS servers: `AmazonProvidedDNS`

You can **create and associate custom DHCP option sets** if your environment requires specific DNS, NTP, or other configurations.

---

## 🎯 Use Case: Using a Custom DNS Server with EC2 Instances

**Scenario**:  
Your organization has internal DNS servers (e.g., running Active Directory) inside a VPC or on-premises. You want all EC2 instances in a VPC to use these DNS servers instead of AWS default DNS.

**Solution**:  
Create a custom DHCP Option Set that points to your internal DNS servers, and associate it with the VPC. EC2 instances will then automatically receive the custom DNS settings.

---

## 🛠️ Steps to Create and Use a DHCP Option Set

### Step 1: Create a Custom DHCP Option Set

1. Open the **AWS Console** → **VPC Dashboard** → **DHCP Option Sets**.
2. Click **"Create DHCP options set"**.
3. Fill in the following:
   - **Domain name**: e.g., `corp.internal`
   - **Domain name servers**: IP addresses of your internal DNS servers  
     _(or use `AmazonProvidedDNS` for default)_
   - (Optional) **NTP servers**, **NetBIOS name servers**, etc.
4. Name the option set (e.g., `custom-dhcp-options`) and click **Create**.

---

### Step 2: Associate the DHCP Option Set with a VPC

1. Go to **VPC Dashboard** → **Your VPCs**.
2. Select the desired VPC.
3. Click **Actions** → **Edit DHCP Options Set**.
4. Choose the newly created option set and click **Save**.

---

### Step 3: Validate the Configuration

1. Launch or restart an **EC2 instance** in the VPC.
2. SSH into the instance and check DNS configuration:
   - **Linux**: View `/etc/resolv.conf`
   - **Windows**: Use `ipconfig /all`

You should see your custom DNS server IPs listed.

---

## 🧠 Notes and Best Practices

- DHCP Option Sets are **region-specific**.
- You **cannot edit** a DHCP option set after creation—create a new one if changes are needed.
- Only instances with **DHCP-based network configuration** (default) will use the settings.
- Ensure **your custom DNS servers are reachable** from the VPC.

---
