# 🧰 AWS Setup Guide: HTTP ALB with VPC, EC2, and Subnets in ap-south-1

This guide walks through creating a full HTTP ALB architecture in AWS Mumbai (`ap-south-1`) region from scratch, including VPC, subnets, routing, security groups, EC2 instances, and an Application Load Balancer.

---

## 🧱 1. Create a VPC

- **Name**: `MyVPC`
- **CIDR Block**: `10.0.0.0/16`
- **Tenancy**: Default

---

## 🌐 2. Create Subnets

| Type    | Name             | AZ          | CIDR Block   |
|---------|------------------|-------------|--------------|
| Public  | PublicSubnet1    | ap-south-1a | 10.0.1.0/24  |
| Public  | PublicSubnet2    | ap-south-1b | 10.0.2.0/24  |
| Private | PrivateSubnet1   | ap-south-1a | 10.0.3.0/24  |
| Private | PrivateSubnet2   | ap-south-1b | 10.0.4.0/24  |

- Enable **Auto-assign Public IP** for **Public** subnets.

---

## 🌐 3. Create Internet Gateway

- Name: `MyIGW`
- Attach to `MyVPC`

---

## 📶 4. Create Route Tables

### Public Route Table
- **Add Route**: `0.0.0.0/0` → **Target**: Internet Gateway (`MyIGW`)
- **Associate** with `PublicSubnet1` and `PublicSubnet2`

### Private Route Table
- No default route yet (NAT gateway added next)
- **Associate** with `PrivateSubnet1` and `PrivateSubnet2`

---

## 🔁 5. Create NAT Gateway

- Allocate a new **Elastic IP**
- Launch **NAT Gateway** in `PublicSubnet1`
- Update **Private Route Table**:
  - **Add Route**: `0.0.0.0/0` → **Target**: NAT Gateway

---

## 🔐 6. Security Groups

### a. ALB Security Group (`ALB-SG`)
- **Inbound Rules**:
  - TCP 80 → Source: `0.0.0.0/0`
- **Outbound Rules**: Allow all

### b. EC2 Security Group (`EC2-SG`)
- **Inbound Rules**:
  - TCP 80 → Source: `ALB-SG`
  - TCP 22, TCP 3389 → Source: `0.0.0.0/0`
- **Outbound Rules**: Allow all

---

## 💻 7. Launch EC2 Instances

- Launch **2 EC2 Instances**:
  - **Instance 1**: in `PrivateSubnet1` (ap-south-1a)
  - **Instance 2**: in `PrivateSubnet2` (ap-south-1b)
- Attach `EC2-SG` Security Group
- Use following **User Data** (Amazon Linux):

```bash
#!/bin/bash
yum install -y httpd
echo "Hello from EC2 in $(hostname)" > /var/www/html/index.html
systemctl enable httpd
systemctl start httpd

🎯 8. Create Target Group
Target type: Instance

Protocol: HTTP

Port: 80

VPC: MyVPC

Health check path: /

Register Targets:

Add both EC2 instances

⚖️ 9. Create Application Load Balancer (ALB)
Name: MyALB

Scheme: Internet-facing

IP Type: IPv4

Listeners: HTTP (80)

VPC: MyVPC

Subnets: PublicSubnet1, PublicSubnet2

Security Group: ALB-SG

Add Listener Rule:

Forward to: Target Group created above

✅ 10. Test the Setup
Open the ALB DNS name in a browser

You should see responses from the EC2 instances

Refresh to test round-robin load balancing

🏁 Done!
Your architecture now looks like:


Internet → ALB (HTTP:80) → EC2s in Private Subnets via Target Group