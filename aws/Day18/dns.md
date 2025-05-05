# 🌐 DNS Resolution Flow Explained

This document explains the **complete DNS resolution process** — from the client to the ISP, Root Servers, TLD servers, and Authoritative Name Servers.

---

## 🧠 What is DNS?

**DNS (Domain Name System)** is like the phonebook of the internet. It translates domain names (e.g., `www.example.com`) into IP addresses (e.g., `93.184.216.34`) that computers use to identify each other.

---

## 📶 Step-by-Step DNS Resolution Process

Let's say you're trying to visit: `www.example.com`

### 🔹 Step 1: Check Local Cache

- Your **computer/browser** checks its local DNS cache.
- ✅ If found: use cached IP.
- ❌ If not found: query the configured **DNS resolver** (ISP or public like 8.8.8.8).

---

### 🔹 Step 2: Query the Recursive Resolver

- The request goes to a **recursive DNS resolver**.
- Usually provided by:
  - Your **ISP**
  - Or public DNS (e.g., Google: `8.8.8.8`, Cloudflare: `1.1.1.1`).

---

### 🔹 Step 3: Query the Root Server

- The recursive resolver asks a **Root DNS Server**:
  > "Where is the TLD server for `.com`?"

- The Root Server replies with the IP address of the **TLD DNS server** for `.com`.

---

### 🔹 Step 4: Query the TLD Server

- Next, the resolver asks the **TLD DNS server**:
  > "Where is the authoritative DNS server for `example.com`?"

- The TLD server replies with the IP of the **authoritative nameserver**.

---

### 🔹 Step 5: Query the Authoritative Nameserver

- The resolver queries the **authoritative nameserver**:
  > "What is the IP address of `www.example.com`?"

- The authoritative server replies:
  > "`www.example.com` is at `93.184.216.34`"

---

### 🔹 Step 6: Return the IP Address to Client

- The resolver returns the final IP address to your computer.
- The IP is **cached locally** for future queries.
- The browser uses the IP to load the website.

---

## 🧾 Summary Diagram

```text
Client (your computer)
    ↓ (no cache)
Recursive Resolver (ISP or public)
    ↓
Root Server (.)
    ↓
TLD Server (.com)
    ↓
Authoritative Nameserver (example.com)
    ↓
Final IP Response (e.g., 93.184.216.34)