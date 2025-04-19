# 📂 Amazon EFS (Elastic File System) – Explained

Amazon EFS (Elastic File System) is a **fully managed, scalable, cloud-native file storage service** provided by AWS. It allows multiple EC2 instances and AWS services to **simultaneously access a shared file system**, just like a network file system in traditional data centers.

---

## 🔸 What is AWS EFS?

- A **managed file storage service** that can be mounted to **multiple EC2 instances**.
- Built on **NFS (Network File System)** protocol.
- Supports **POSIX-compliant file systems**, ideal for Linux workloads.
- Provides **elastic storage** — scales automatically as you add/remove files.
- Supports access from **multiple Availability Zones (AZs)** for **high availability** and **durability**.

---

## 🔸 Key Features

| Feature                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **Elastic Storage**      | Automatically grows and shrinks with file usage. No provisioning needed.   |
| **Fully Managed**        | No servers to manage — AWS handles maintenance, updates, backups.          |
| **Multi-AZ Access**      | Accessible across multiple AZs in a region for high availability.          |
| **Simultaneous Access**  | Mount to multiple EC2 instances at once — great for shared workloads.      |
| **POSIX-compliant**      | Supports Linux file permissions, symlinks, and directory structures.       |
| **Secure**               | Supports IAM, VPC, encryption at rest/in-transit, and access points.       |

---

## 🔸 Common Use Cases

- **Web server content hosting**
- **Home directories for multiple users**
- **Container storage** (ECS, EKS)
- **Big data and analytics**
- **Lift-and-shift enterprise apps**

---

## 🔸 EFS vs Other AWS Storage

| AWS Service | Storage Type | Description                                   | Shared Access |
|-------------|---------------|-----------------------------------------------|----------------|
| **EBS**     | Block         | Attached to one EC2 instance at a time        | ❌              |
| **S3**      | Object        | For storing individual objects/files (S3 API) | ❌              |
| **EFS**     | File          | Mountable file system across EC2s             | ✅              |

---

## 🔸 Pricing Model

- **Pay-as-you-go** based on:
  - GBs stored per month
  - Optional features like provisioned throughput or storage tiers
- **Lifecycle management** helps reduce cost by automatically moving inactive files to infrequent access storage.

---

## 🔸 How It Works (Simplified)

1. You create an **EFS file system** in your VPC.
2. AWS automatically creates **mount targets** in each Availability Zone.
3. You **mount** the file system on your EC2 instances using the NFS protocol.
4. Your apps can now read/write files just like a local drive — but it’s actually cloud storage!

---

## 🔸 Summary

Amazon EFS is perfect for:
- Applications that require **shared file access**
- Scalable and elastic workloads
- High-availability storage needs across AZs

It’s like plugging multiple EC2 instances into the **same network drive** — simple, scalable, and reliable.
