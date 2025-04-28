# 📘 Understanding IPv4 Address Schemes: Classful, Classless, and Subnetting

## 1. 🧠 What is an IPv4 Address?

An **IPv4 address** is a 32-bit number used to identify devices on a network. It's written in **dotted decimal format**, like:

192.168.1.1

Each IPv4 address has two parts:
- **Network portion**: Identifies the network
- **Host portion**: Identifies the device on that network

---

## 2. 📦 Classful Addressing (Old System)

Classful addressing divides the IPv4 space into five classes (A to E), but the most commonly used are A, B, and C.

| Class | First Octet Range | Default Subnet Mask | Network/Host bits | Example        |
|-------|-------------------|----------------------|-------------------|----------------|
| A     | 1 - 126           | 255.0.0.0            | 8 bits / 24 bits  | 10.0.0.1       |
| B     | 128 - 191         | 255.255.0.0          | 16 bits / 16 bits | 172.16.0.1     |
| C     | 192 - 223         | 255.255.255.0        | 24 bits / 8 bits  | 192.168.1.1    |

> 💡 **Note**: 127.x.x.x is reserved for loopback testing.

### ❗ Problem with Classful:
It wastes IP addresses. For example, if you only need 20 IPs, Class C still gives you 254!

---

## 3. 🚫 Classless Addressing (CIDR)

**CIDR** = Classless Inter-Domain Routing

CIDR allows flexible allocation of IPs by using **slash notation** (prefix length):

192.168.1.0/24 → subnet mask: 255.255.255.0

yaml
Copy
Edit

| CIDR      | Subnet Mask        | # of Hosts |
|-----------|--------------------|------------|
| /30       | 255.255.255.252    | 2          |
| /29       | 255.255.255.248    | 6          |
| /28       | 255.255.255.240    | 14         |
| /24       | 255.255.255.0      | 254        |
| /16       | 255.255.0.0        | 65,534     |

---

## 4. 🧮 Subnetting Basics

**Subnetting** = Dividing a network into smaller sub-networks for:

- Better performance
- Improved security
- Efficient IP usage

### 📌 Key Formulas:
- **Number of subnets** = 2ⁿ (n = number of subnet bits borrowed)
- **Hosts per subnet** = 2ʰ - 2 (h = number of host bits left)

---

## 5. 📘 Subnetting Examples

### ✅ Example 1: Creating 4 Subnets from /24

- Original: `192.168.1.0/24`
- Want: 4 subnets
- Borrow 2 bits → /26
- Subnet mask: `255.255.255.192`
- Block size: 64

| Subnet        | Usable IP Range        | Broadcast Address |
|---------------|------------------------|-------------------|
| 192.168.1.0/26 | 192.168.1.1 - .62      | 192.168.1.63      |
| 192.168.1.64/26 | 192.168.1.65 - .126    | 192.168.1.127     |
| 192.168.1.128/26 | 192.168.1.129 - .190  | 192.168.1.191     |
| 192.168.1.192/26 | 192.168.1.193 - .254  | 192.168.1.255     |

---

### ✅ Example 2: Need at Least 30 Hosts per Subnet

- Use: 2⁵ - 2 = 30 → /27
- Subnet mask: `255.255.255.224`
- Hosts per subnet: 30
- Block size: 32

---

### ✅ Example 3: Create 8 Subnets from a /24 Network

**Given:**
- Network: `192.168.10.0/24`
- Need: **8 subnets**

**Borrow 3 bits → /27 → Subnet mask: 255.255.255.224**

| Subnet # | Network Address | First Usable | Last Usable | Broadcast Address |
|----------|------------------|--------------|-------------|-------------------|
| 1        | 192.168.10.0     | 192.168.10.1 | 192.168.10.30 | 192.168.10.31   |
| 2        | 192.168.10.32    | 192.168.10.33 | 192.168.10.62 | 192.168.10.63  |
| 3        | 192.168.10.64    | 192.168.10.65 | 192.168.10.94 | 192.168.10.95  |
| ...      | ...              | ...           | ...          | ...               |

---

### ✅ Example 4: Need at Least 100 Hosts per Subnet

- Use: 2⁷ - 2 = 126 → /25
- Subnet mask: `255.255.255.128`

| Subnet # | Network Address | Usable IP Range         | Broadcast Address |
|----------|------------------|-------------------------|-------------------|
| 1        | 10.0.0.0/25      | 10.0.0.1 - 10.0.0.126   | 10.0.0.127         |
| 2        | 10.0.0.128/25    | 10.0.0.129 - 10.0.0.254 | 10.0.0.255         |

---

### ✅ Example 5: Find Subnet Info for 172.16.50.10/20

- Subnet mask: `255.255.240.0`
- Block size: 16 → 172.16.48.0 - 172.16.63.255

| Field              | Value                |
|--------------------|----------------------|
| Network Address    | 172.16.48.0          |
| Broadcast Address  | 172.16.63.255        |
| Usable IP Range    | 172.16.48.1 - .254   |

---

### ✅ Example 6: VLSM (Variable Length Subnet Masking)

**Given:**
- Network: `192.168.1.0/24`
- Requirements:
  - Subnet A: 100 hosts → /25
  - Subnet B: 50 hosts → /26
  - Subnet C: 25 hosts → /27

**Allocate accordingly:**

| Subnet | Network            | Usable Range                | Broadcast       |
|--------|--------------------|-----------------------------|-----------------|
| A      | 192.168.1.0/25     | 192.168.1.1 - 192.168.1.126 | 192.168.1.127   |
| B      | 192.168.1.128/26   | 192.168.1.129 - .190        | 192.168.1.191   |
| C      | 192.168.1.192/27   | 192.168.1.193 - .222        | 192.168.1.223   |

---

## 📎 Summary

- **Classful addressing** is outdated and inefficient.
- **CIDR** allows flexible subnetting using prefix lengths.
- **Subnetting** helps divide networks efficiently.
- **VLSM** allows different subnets to have different sizes based on need.