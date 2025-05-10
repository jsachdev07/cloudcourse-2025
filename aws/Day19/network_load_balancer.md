
### 🧰 AWS Network Load Balancer (NLB) Full Setup Guide
Use Case: Set up a Network Load Balancer to forward TCP traffic on port 80 to two EC2 instances running a basic Apache HTTP server.

### 🧭 What is a Network Load Balancer (NLB)?
Operates at Layer 4 (Transport Layer).

Supports TCP, UDP, and TLS.

Designed for high-performance and low-latency use cases.

Routes traffic purely based on IP and port, without inspecting the request (no HTTP headers, cookies, etc.).

### 📌 Architecture Overview

            +-----------------------------+
            |     Network Load Balancer  |
            |      (TCP on Port 80)       |
            +-----------------------------+
               |                    |
      +--------+--------+   +--------+--------+
      | EC2: WebServer1 |   | EC2: WebServer2 |
      | Apache on port 80|  | Apache on port 80|
      +------------------+   +-----------------+
### 🖥️ PART 1: Launch EC2 Instances with Apache
We'll launch two EC2 instances with Apache to serve HTTP content on port 80.

🔹 Step-by-Step: Create EC2 Instances
Go to EC2 → Instances → Launch Instances

Instance Name: WebServer-1 and WebServer-2 (launch two instances)

AMI: Amazon Linux 2 (free tier)

Instance Type: t2.micro (free tier)

Key Pair: Select or create a key pair for SSH access

Network Settings:

Choose a VPC and public subnet

Enable auto-assign public IP

Create or choose a security group:

Inbound rule: allow TCP port 80 from 0.0.0.0/0

User Data Script (for Apache install):
```
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from $(hostname)</h1>" > /var/www/html/index.html
Click Launch
```
Repeat for both instances.

### 🧩 PART 2: Create Target Group (TCP)
Target groups in NLB are responsible for managing where the traffic goes (your EC2 instances).

🔹 Steps:
Go to EC2 → Target Groups → Create Target Group

Settings:

Target type: Instance

Protocol: TCP

Port: 80

VPC: Your VPC where EC2s are deployed

Name: nlb-tcp-group

Click Next

Register Targets:

Select both EC2 instances

Port: 80

Click Create target group

### 🌐 PART 3: Create Network Load Balancer
🔹 Steps:
Go to EC2 → Load Balancers → Create Load Balancer

Choose: Network Load Balancer

Fill in the details:

Name: my-nlb

Scheme: Internet-facing

IP Type: IPv4

Listeners:

Protocol: TCP

Port: 80

Availability Zones:

Select at least 2 zones

Associate with public subnets

Target Group Association:

Listener → Forward to nlb-tcp-group

Click Create Load Balancer

### 🔍 PART 4: Test NLB
🔹 Get the NLB DNS Name:
Go to EC2 → Load Balancers

Find your Network Load Balancer

Copy the DNS name, something like:

perl
Copy
Edit
my-nlb-1234567890.us-east-1.elb.amazonaws.com
🔹 Open in Browser:
Visit:

arduino
Copy
Edit
http://my-nlb-1234567890.us-east-1.elb.amazonaws.com
You should see:

<h1>Hello from ip-172-31-xx-xx</h1>


### 📍 Important Notes
Feature	NLB Support
Host-based routing	❌ No
Path-based routing	❌ No
SSL termination	✅ Yes (TLS Listener)
HTTP headers inspection	❌ No
IP-based target support	✅ Yes
Static IPs via EIPs	✅ Optional

### 🛡️ Security Group Settings
Ensure your EC2 instance’s security group allows inbound traffic on port 80 from 0.0.0.0/0 or from the NLB's VPC CIDR block if private.

### ⚠️ NLB does not associate with a security group itself (unlike ALB). It just forwards raw TCP traffic to targets.
