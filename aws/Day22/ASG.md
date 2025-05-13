# AWS Basic EC2 Auto Scaling
Basic step-by-step guide to creating an EC2 instance and configuring Auto Scaling in AWS:

### **Step 1: Create an EC2 Instance**

1. **Login to AWS Console:**
   - Go to the [AWS Management Console](https://aws.amazon.com/console/) and sign in with your credentials.

2. **Navigate to EC2 Service:**
   - On the AWS Management Console dashboard, search for **EC2** in the "Find Services" bar and select **EC2**.

3. **Launch Instance:**
   - Click on **Launch Instance**.

4. **Choose an Amazon Machine Image (AMI):**
   - Select an AMI that suits your needs, such as **Amazon Linux 2**, **Ubuntu**, or **Windows Server**.
   - You can use **Free Tier eligible AMIs** if you're testing or learning.

5. **Choose an Instance Type:**
   - Select the instance type. For basic usage, the **t2.micro** or **t3.micro** (if eligible) instance type is commonly used.
   - Click **Next: Configure Instance Details**.

6. **Configure Instance Details:**
   - Here, you can configure network settings like VPC and subnet. For a default setup, you can leave these as they are.
   - For Auto Scaling later, ensure that you choose the **default VPC** or a VPC that Auto Scaling can access.
   - Click **Next: Add Storage**.

7. **Add Storage:**
   - By default, the AMI will come with a certain amount of EBS (Elastic Block Store). You can modify the storage size as needed.
   - Click **Next: Add Tags**.

8. **Add Tags:**
   - Tags help identify your instance. Add key-value pairs like `Name=MyEC2Instance`.
   - Click **Next: Configure Security Group**.

9. **Configure Security Group:**
   - Set rules for your instance security. For example, allow SSH (port 22) for Linux instances or RDP (port 3389) for Windows.
   - Allow HTTP/HTTPS traffic if you're setting up a web server.
   - Click **Review and Launch**.

10. **Review and Launch:**
    - Review all the configuration details. If everything looks good, click **Launch**.

11. **Select/Create a Key Pair:**
    - Choose an existing key pair or create a new one. This is important for SSH/RDP access.
    - **Download the key pair** if you created a new one (you won’t be able to download it later).
    - Click **Launch Instances**.

12. **Access the Instance:**
    - Once the instance is launched, you can access it by using SSH (for Linux) or RDP (for Windows) using the public IP address of the instance.

---

### **Step 2: Configure Auto Scaling**

Auto Scaling automatically adjusts the number of EC2 instances based on traffic and usage patterns.

#### **Part 1: Create a Launch Template (for Auto Scaling)**

1. **Navigate to EC2 Dashboard:**
   - In the EC2 console, click **Launch Templates** under the **Instances** section.

2. **Create Launch Template:**
   - Click **Create Launch Template**.
   
3. **Template Name and Description:**
   - Enter a name for the template (e.g., `MyLaunchTemplate`) and an optional description.
   
4. **Source AMI:**
   - Choose the AMI (Amazon Machine Image) you want to use. This could be the same AMI you selected earlier for the EC2 instance.
   
5. **Instance Type:**
   - Select the instance type (e.g., `t2.micro` or `t3.micro`).

6. **Key Pair:**
   - Choose the same key pair you selected when launching the EC2 instance, so you can access the instances.

7. **Network Settings:**
   - Configure the VPC, subnet, and security group. This should match the VPC and security group you configured for the EC2 instance.

8. **Storage (EBS):**
   - Configure the same storage settings as your EC2 instance, or adjust according to your needs.

9. **Tags:**
   - Add tags for your instance, such as `Name=AutoScalingInstance`.

10. **Create Launch Template:**
    - Once you have filled in all the required fields, click **Create Launch Template**.

---

#### **Part 2: Create an Auto Scaling Group**

1. **Navigate to Auto Scaling:**
   - In the EC2 dashboard, click **Auto Scaling Groups** under the **Auto Scaling** section.

2. **Create Auto Scaling Group:**
   - Click **Create Auto Scaling group**.

3. **Select Launch Template:**
   - Choose **Launch Template** and select the template you created earlier.

4. **Auto Scaling Group Name:**
   - Enter a name for the Auto Scaling group (e.g., `MyAutoScalingGroup`).

5. **VPC and Subnets:**
   - Choose the VPC and subnets where your instances will be launched. This should be the same as the VPC for your original EC2 instance.

6. **Configure Scaling Policies:**
   - Choose the desired scaling policies. You can select:
     - **Target Tracking Scaling**: Automatically adjust the number of instances to maintain a target CPU utilization.
     - **Step Scaling**: Scale based on specified alarms (like when CPU usage reaches a threshold).
     - **Scheduled Scaling**: Set specific times to scale up or down.

7. **Set Desired, Minimum, and Maximum Capacity:**
   - **Desired Capacity**: The number of instances to run initially (e.g., 1 or 2).
   - **Minimum Capacity**: The minimum number of instances (e.g., 1).
   - **Maximum Capacity**: The maximum number of instances that Auto Scaling can scale up to (e.g., 5).

8. **Health Checks:**
   - Enable **EC2 health checks** to replace unhealthy instances automatically.

9. **Notifications (Optional):**
   - You can configure SNS (Simple Notification Service) to send notifications when instances are launched or terminated.

10. **Review and Create:**
    - Review all configurations and click **Create Auto Scaling group**.

---

### **Step 3: Verify Auto Scaling Behavior**

1. **Test Scaling:**
   - You can trigger scaling by creating load or adjusting the desired capacity.
   - Use AWS CloudWatch to monitor instance performance (e.g., CPU utilization). If the CPU usage exceeds the threshold defined in your scaling policy, new instances should automatically launch.

2. **Check Instances:**
   - Navigate to the **EC2 Instances** section in the console to see the instances created by Auto Scaling.

3. **Scaling Events:**
   - In the **Auto Scaling Groups** dashboard, check the **Activity** tab to view the scaling events.

---

### Desired Capacity, Minimum Capacity, and Maximum Capacity are key parameters that control how many EC2 instances are managed by an **Auto Scaling Group (ASG)** in AWS. Let's break each one down, followed by a detailed example:

---

### **1. Minimum Capacity:**
- **Definition:** This is the minimum number of instances that the Auto Scaling group will always maintain. Even if there is low traffic or resource utilization, AWS will not terminate instances below this number.
- **Use Case:** You set the **Minimum Capacity** to ensure that your application always has a certain number of instances running to handle base-level traffic.

### **2. Maximum Capacity:**
- **Definition:** This is the maximum number of instances that the Auto Scaling group can scale up to. When traffic increases or resource utilization spikes, Auto Scaling will launch more instances, but it will not exceed this number.
- **Use Case:** You set the **Maximum Capacity** to control your AWS cost and resource usage, as adding more instances beyond this point could be unnecessary or too costly.

### **3. Desired Capacity:**
- **Definition:** This is the target number of instances that you want running at any given moment. The Auto Scaling group will attempt to maintain this number of instances. If the desired capacity is set higher than the current number of instances, Auto Scaling will launch more instances to meet the desired count. If it’s set lower, Auto Scaling will terminate instances to reduce the number.
- **Use Case:** You set the **Desired Capacity** to reflect the normal operational needs of your application. This number can change dynamically based on scaling policies.

---

### **Example Scenario**

Let’s say you have an application that experiences variable traffic loads, and you’ve configured an Auto Scaling Group (ASG) with the following settings:

- **Minimum Capacity:** 2
- **Maximum Capacity:** 10
- **Desired Capacity:** 4

Here’s how the ASG would behave in different situations:

---

### **Case 1: Normal Traffic (Desired Capacity)**

- **Initial Condition:** Your application is receiving a moderate amount of traffic, and you expect the ASG to maintain 4 instances to handle it.
  
- **Outcome:** 
  - The ASG will launch 4 EC2 instances (matching the Desired Capacity).
  - These 4 instances will remain running as long as traffic remains stable and no scaling event occurs.
  
### **Case 2: Low Traffic (Scaling Down)**

- **Event:** Suppose traffic drops significantly, and your scaling policy triggers to reduce the number of instances.

- **Outcome:**
  - The ASG will attempt to reduce the number of instances.
  - However, it **cannot go below the Minimum Capacity** (2 in this case), so the ASG will terminate 2 instances and maintain 2 instances.
  - This ensures that even during low traffic, there are always at least 2 instances running.

---

### **Case 3: High Traffic (Scaling Up)**

- **Event:** Now let’s assume traffic surges due to a flash sale, and resource utilization (like CPU or memory) increases beyond the threshold set in your scaling policy.

- **Outcome:**
  - The ASG will launch additional instances to handle the increased load.
  - If the Desired Capacity (4 instances) is no longer enough, Auto Scaling will increase the instance count, potentially up to 10 instances (which is the **Maximum Capacity**).
  - However, the ASG **cannot exceed the Maximum Capacity**. Even if traffic increases further, the group will not launch more than 10 instances.
  
### **Case 4: Manual Adjustment of Desired Capacity**

- **Event:** Let’s say you decide that your application needs to run 6 instances at all times (possibly because you’re anticipating a new marketing campaign).
  
- **Action:** You manually adjust the **Desired Capacity** from 4 to 6.
  
- **Outcome:**
  - The ASG will launch 2 more instances to meet the new desired count.
  - If traffic increases beyond capacity, the ASG will continue scaling up to 10 instances, but it won't fall below 6 until you change the Desired Capacity again or if there is a scaling policy that triggers further adjustments.

---

### **Summary:**

- **Minimum Capacity:** The group will never go below this number, even if traffic is very low.
- **Desired Capacity:** The group will try to maintain this number of instances under normal circumstances.
- **Maximum Capacity:** The group will never scale beyond this number, even during high-traffic spikes.

---

### **Example Recap**

- With **Minimum Capacity** set to **2**, your Auto Scaling group will always have at least 2 EC2 instances running.
- With **Desired Capacity** set to **4**, your ASG will maintain 4 instances under normal traffic conditions.
- With **Maximum Capacity** set to **10**, your ASG will scale up as traffic increases, but it won’t exceed 10 instances no matter how high the traffic goes.

These parameters ensure you have a baseline number of instances for low traffic, flexibility to scale as demand grows, and a ceiling to prevent runaway scaling and control costs.
