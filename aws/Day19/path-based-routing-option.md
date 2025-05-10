🛠️ AWS ALB Path-Based Routing Setup with EC2 and Apache
This guide sets up an Application Load Balancer (ALB) to route traffic between two EC2 web servers based on URL paths using the domain devcloudhub.info.

📌 Overview
Path	Target EC2	Page Message
/app1	WebServer-App1	Welcome to the App1 page
/app2	WebServer-App2	Welcome to the App2 page

📦 PART 1: Launch EC2 Instances with Apache
🔹 EC2 Instance 1: WebServer-App1
Launch EC2 Instance

AMI: Amazon Linux 2

Instance Type: t2.micro

Name: WebServer-App1

Enable auto-assign public IP

Security Group: Allow HTTP (80) and SSH (22)

User Data Script (Paste into Advanced → User Data):

bash
Copy
Edit
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd 
systemctl enable httpd
mkdir -p /var/www/html/app1
echo "<h1> Welcome to the App1 page of Web Server </h1>" > /var/www/html/app1/index.html
🔹 EC2 Instance 2: WebServer-App2
Launch EC2 Instance

AMI: Amazon Linux 2

Instance Type: t2.micro

Name: WebServer-App2

Use the same settings as App1

User Data Script:

bash
Copy
Edit
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd 
systemctl enable httpd
mkdir -p /var/www/html/app2
echo "<h1> Welcome to the App2 page of Web Server </h1>" > /var/www/html/app2/index.html
🎯 PART 2: Create Target Groups
Go to EC2 → Target Groups → Create Target Group

🔸 Target Group: tg-app1
Type: Instances

Protocol: HTTP

Port: 80

Register: WebServer-App1

🔸 Target Group: tg-app2
Type: Instances

Protocol: HTTP

Port: 80

Register: WebServer-App2

🌐 PART 3: Create Application Load Balancer (ALB)
Go to EC2 → Load Balancers → Create Load Balancer

Choose: Application Load Balancer

Name: devcloudhub-alb

Scheme: Internet-facing

Listener: HTTP (port 80)

Availability Zones: Choose zones with your EC2s

Security Group: Allow HTTP (port 80)

🔀 PART 4: Configure ALB Listener Rules
Go to Load Balancer → Listeners → View/Edit Rules

Add Rules:

➤ Rule for /app1/*
Condition: Path is /app1/*

Action: Forward to tg-app1

➤ Rule for /app2/*
Condition: Path is /app2/*

Action: Forward to tg-app2

Keep default action as fixed response or remove

🌍 PART 5: Set Up DNS in Route 53
Go to Route 53 → Hosted Zones → devcloudhub.info

Click Create Record

Type: A – IPv4

Alias: Yes

Alias Target: Select the ALB DNS name

Record Name: Leave empty (for root domain)

✅ PART 6: Test the Setup
Open in browser:

http://devcloudhub.info/app1 → should show App1 welcome page

http://devcloudhub.info/app2 → should show App2 welcome page