# Public IP vs Elastic IP in AWS

## 1. Public IP
A **Public IP** in AWS refers to an IP address that can be used to communicate with your EC2 instance over the internet. It's automatically assigned when you launch an EC2 instance, and it’s dynamic, meaning it can change when the instance is stopped and restarted.

### Key Characteristics of Public IP:
- **Dynamic**: It changes when you stop and start your instance.
- **Temporary**: It’s not static, so you lose the IP when the instance is stopped or terminated.
- **Assigned automatically**: AWS automatically assigns a public IP when you launch an EC2 instance in a VPC (Virtual Private Cloud).
- **Not transferable**: You cannot move the public IP to another instance; it’s directly associated with the instance when it's launched.

### How Public IP Works:
- When you launch an instance in a public subnet, AWS assigns a public IP address to that instance. You can use this IP to connect to the instance over the internet.
- It is temporary, so once the instance is stopped or terminated, the public IP is released.

## 2. Elastic IP (EIP)
An **Elastic IP** (EIP) is a static, public IPv4 address designed for dynamic cloud computing. You can associate it with an EC2 instance, and it does not change even if you stop and restart the instance. Elastic IPs allow you to remap the address to different instances, making them useful for high-availability setups or failover scenarios.

### Key Characteristics of Elastic IP:
- **Static**: The IP does not change when the instance is stopped or started.
- **Persistent**: You own the Elastic IP and can retain it until you choose to release it.
- **Transferable**: You can move the Elastic IP between instances in your account.
- **Cost**: AWS charges for Elastic IP if it’s not associated with a running instance.

### How Elastic IP Works:
- You can allocate an Elastic IP to your AWS account and then associate it with a running EC2 instance.
- Even if you stop or start the instance, the Elastic IP will not change, ensuring that your application has a fixed IP address.
- If you need to move the Elastic IP to another instance, you can simply disassociate it from one instance and associate it with another instance.

## Differences Between Public IP and Elastic IP:

| **Feature**                | **Public IP**                                          | **Elastic IP (EIP)**                                |
|----------------------------|--------------------------------------------------------|-----------------------------------------------------|
| **Assigned Automatically**  | Yes (when you launch the instance in a VPC)            | No, you need to allocate it yourself                |
| **Persistence**             | No, it changes if the instance is stopped and restarted | Yes, it remains the same even if the instance is stopped and restarted |
| **Transferable**            | No, it’s tied to the instance                         | Yes, you can move it between instances             |
| **Cost**                    | Free (if associated with a running instance)           | Free, but charged if not associated with a running instance |
| **Use Case**                | Temporary internet access for instances                | Long-term, static IP for high availability or failover scenarios |

## How to Use Elastic IP in AWS

### Step 1: Allocate an Elastic IP
1. Open the **Amazon EC2 Console**.
2. In the left sidebar, under **Network & Security**, click on **Elastic IPs**.
3. Click on the **Allocate Elastic IP address** button.
4. Choose the **Amazon pool of IPv4 addresses** and click **Allocate**.

### Step 2: Associate Elastic IP with an EC2 Instance
1. After allocating the Elastic IP, select it in the **Elastic IPs** dashboard.
2. Click on the **Actions** button, then choose **Associate Elastic IP address**.
3. In the **Instance** field, select the instance you want to associate the Elastic IP with.
4. Optionally, choose the private IP if your instance has more than one.
5. Click **Associate**.

### Step 3: Disassociate or Release an Elastic IP
- To disassociate an Elastic IP from an instance, simply go to the **Elastic IPs** dashboard, select the Elastic IP, click **Actions**, and choose **Disassociate**.
- To release an Elastic IP, select the IP and click **Release** under **Actions**.

## Best Practices for Elastic IPs
- **Use Elastic IPs only when needed**: Since AWS charges for Elastic IPs when they are not associated with a running instance, it's best to only use them when necessary.
- **Keep a record of your Elastic IPs**: If you have multiple Elastic IPs, track their usage so you can efficiently manage them.

## When to Use Elastic IP
- **High Availability**: If you want to ensure that your EC2 instances always have the same IP address (even if the instance is stopped and restarted).
- **Failover**: You can remap an Elastic IP to a different EC2 instance if the current one fails, ensuring minimal downtime.

### Example of Use:
Imagine you're running a website on an EC2 instance, and you want to ensure that users can always access it via the same IP. You could associate an Elastic IP with the instance. Even if you stop and start the instance for maintenance, the Elastic IP ensures the website is always reachable using the same IP address.
---