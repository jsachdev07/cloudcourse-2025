🛠️ AWS ALB Host-Based Routing Setup with EC2 and Apache
This guide walks you through creating two EC2 instances, configuring Apache on each, and setting up an ALB to route traffic based on hostnames (subdomains) like app1.devcloudhub.info and app2.devcloudhub.info.

📌 Overview
Hostname	Target EC2	Page Message
app1.devcloudhub.info	WebServer-App1	Welcome to the App1 page
app2.devcloudhub.info	WebServer-App2	Welcome to the App2 page

📦 PART 1: Launch EC2 Instances with Apache
🔹 EC2 Instance 1: WebServer-App1
Launch EC2 Instance

AMI: Amazon Linux 2

Type: t2.micro

Name: WebServer-App1

Enable auto-assign public IP

Security Group: Allow HTTP (80) and SSH (22)

User Data Script (Advanced → User data):

bash
Copy
Edit
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd 
systemctl enable httpd
echo "<h1> Welcome to the App1 page of Web Server </h1>" > /var/www/html/index.html
🔹 EC2 Instance 2: WebServer-App2
Launch EC2 Instance

Same configuration as App1

Name: WebServer-App2

User Data Script:

bash
Copy
Edit
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd 
systemctl enable httpd
echo "<h1> Welcome to the App2 page of Web Server </h1>" > /var/www/html/index.html
🎯 PART 2: Create Target Groups
Go to EC2 → Target Groups → Create Target Group

🔸 tg-app1
Target Type: Instances

Protocol: HTTP

Port: 80

Register: WebServer-App1

🔸 tg-app2
Target Type: Instances

Protocol: HTTP

Port: 80

Register: WebServer-App2

🌐 PART 3: Create Application Load Balancer (ALB)
Go to EC2 → Load Balancers → Create Load Balancer

Select: Application Load Balancer

Name: devcloudhub-alb

Scheme: Internet-facing

Listener: HTTP (80)

Availability Zones: Choose zones with your EC2s

Security Group: Allow HTTP (80)

🔀 PART 4: Configure ALB Listener Rules (Host-Based)
After ALB is created, go to Listeners → View/Edit Rules

Add these host-based rules:

➤ Rule 1: Host = app1.devcloudhub.info
Action: Forward to tg-app1

➤ Rule 2: Host = app2.devcloudhub.info
Action: Forward to tg-app2

🌍 PART 5: Configure DNS in Route 53
Go to Route 53 → Hosted Zone → devcloudhub.info

Create Records:
➤ Record 1
Name: app1.devcloudhub.info

Type: A (Alias)

Alias: Yes

Target: ALB DNS name

➤ Record 2
Name: app2.devcloudhub.info

Type: A (Alias)

Alias: Yes

Target: ALB DNS name

✅ Ensure your DNS TTL is low during testing (e.g., 60 seconds)

✅ PART 6: Test the Setup
In your browser, visit:

http://app1.devcloudhub.info → should load App1 welcome page

http://app2.devcloudhub.info → should load App2 welcome page