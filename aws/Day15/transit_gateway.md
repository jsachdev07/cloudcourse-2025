# AWS Transit Gateway – Use Case and Step-by-Step Guide

---

## ✅ Use Case: Centralized Network Hub for Multi-VPC Communication

**Scenario**:  
A company has multiple AWS accounts and VPCs across different regions used by various departments (e.g., Dev, QA, Prod). Each VPC requires secure communication with others, and potentially with on-premises networks via Direct Connect or VPN.

**Solution**:  
Use **AWS Transit Gateway** as a **central routing hub**, simplifying VPC peering, reducing route table complexity, and enabling scalable, transitive communication between networks.

---

## 🛠️ Steps to Create and Use AWS Transit Gateway

### Step 1: Create the Transit Gateway

1. Go to **AWS Console** → **VPC Dashboard** → **Transit Gateways**.
2. Click **"Create Transit Gateway"**.
3. Provide the following:
   - **Name tag**: `central-tgw`
   - **Amazon ASN**: (leave default or specify for BGP)
   - Enable/disable options as needed:
     - **Auto-accept shared attachments**: Yes (optional)
     - **Default route table association**: Yes
     - **DNS support**: Enable
4. Click **Create Transit Gateway**.

---

### Step 2: Create Attachments to VPCs

1. Go to **Transit Gateway Attachments** → **Create attachment**.
2. Select:
   - **Transit Gateway** (created above)
   - **Attachment type**: VPC
   - **VPC ID**: Choose the VPC to attach
   - **Subnets**: Select at least one subnet per AZ
3. Click **Create attachment**.
4. Repeat for each VPC that needs to connect.

> 💡 You can also create **VPN** or **Direct Connect** attachments for hybrid connections.

---

### Step 3: Accept Attachments (if cross-account)

- If VPCs are in **different AWS accounts**, use **AWS Resource Access Manager (RAM)** to share the Transit Gateway.
- In the target account:
  - **Accept the resource share**
  - **Accept the attachment**

---

### Step 4: Configure Transit Gateway Route Tables

1. Go to **Transit Gateway Route Tables**.
2. Use the **default route table** or create a new one.
3. For each VPC attachment:
   - **Associate** the attachment with the route table.
   - Add **routes** to other VPCs, VPNs, or on-prem destinations.

---

### Step 5: Update VPC Route Tables

1. Go to **VPC → Route Tables**.
2. For each VPC:
   - Edit the route table associated with the relevant subnet(s).
   - Add a route to the **CIDR block** of other VPCs.
   - Target: **Transit Gateway ID**

---

### Step 6: (Optional) Monitor and Secure

- Enable **VPC Flow Logs** for monitoring.
- Use **CloudWatch** to track Transit Gateway metrics.
- Manage **cross-account access** with **AWS RAM**.
- Apply **Security Groups** and **NACLs** as needed.

---

## 🔁 Example: 3-VPC Architecture

You have 3 VPCs:
- **Dev**: `10.0.0.0/16`
- **QA**: `10.1.0.0/16`
- **Prod**: `10.2.0.0/16`

By attaching all to a single Transit Gateway and configuring the routing, all three can communicate **transitively**, with simplified management compared to VPC peering.

---