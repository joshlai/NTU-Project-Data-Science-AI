# 🚀 VM Setup and Environment Initialization Guide

This guide provides step-by-step instructions to spin up a GCP VM instance with:

- ✅ **2 vCPUs**
- ✅ **10GB HDD**
- ✅ **4GB RAM**

This environment is suitable for running **Dagster**, **Python**, and **DBT**.

> ⚠️ **Note:** Your local project structure must match exactly to avoid issues.

---

## 🧭 Step-by-Step Instructions

### 🔹 Step 1: Launch Compute Engine
In the GCP Console, search for **Compute**:  
![Compute Search](image.png)

### 🔹 Step 2: Open Compute Engine
Select **Compute Engine**:  
![Compute Engine](image-1.png)

### 🔹 Step 3: Access the Dashboard
You’ll land on the Compute Engine dashboard:  
![Dashboard](image-2.png)

### 🔹 Step 4: Launch Google Cloud Shell
Click the **Cloud Shell** icon on the top-right:  
![Cloud Shell](image-3.png)

### 🔹 Step 5: Wait for Cloud Shell to Load
Cloud Shell is launched:  
![Cloud Shell Terminal](image-4.png)

---

### 🔹 Step 6: Upload Setup Script
Upload `create-vm.sh` from the `IAC` folder to the terminal:  
![Upload Script](image-5.png)

### 🔹 Step 7: Check for Upload
Use `ls` to verify the upload. The file should appear in white:  
![List Files](image-6.png)

### 🔹 Step 8: Make Executable
Run the following to make it executable:
```bash
chmod +x create-vm.sh
ls
```
File should now be green:  
![Executable File](image-7.png)

### 🔹 Step 9: Run the Script
```bash
./create-vm.sh
```
Ignore the disk size warning:  
![Script Running](image-8.png)

### 🔹 Step 10: Refresh VM Console
Click **VM Instances** to view the VM:  
![VM Instances](image-9.png)

### 🔹 Step 11: Confirm VM Creation
Check for a VM named `vm-etl-2`:  
![VM Created](image-10.png)

---

### 🔹 Step 12 (Optional): Stop VM to Prevent Charges
Click the 3 dots → **Stop VM** if you're not continuing:  
![Stop VM](image-11.png)

### 🔹 Step 13: Open VM
Click on the created VM:  
![Open VM](image-12.png)

### 🔹 Step 14: Connect via SSH
Click **SSH** and authorize:  
![SSH](image-15.png)

---

## 🗂️ File Upload & Environment Setup

### 🔹 Step 15: Create Project Directory
```bash
cd ~
mkdir biscuit
cd biscuit
```
![Make Directory](image-13.png)

### 🔹 Step 16: Upload Files and Run Setup
Upload `environment.yml` and `setup.sh`. Then:
```bash
chmod +x setup.sh
./setup.sh
```
![Run Setup](image-16.png)

### 🔹 Step 17: Restart Services
Select both services to restart:  
![Restart Services](image-17.png)

### 🔹 Step 18: Choose Desktop Environment
Select **lightdm** and reboot.

---

## 🐍 Python Environment & GitHub Setup

### 🔹 Step 19: Create Conda Environment
```bash
conda env create -f environment.yml
```

### 🔹 Step 20: Activate Conda Environment
```bash
conda activate <your_env_name>
```

### 🔹 Step 21: Generate SSH Key
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Press Enter 3 times to accept defaults.  


### 🔹 Step 22: Copy Public Key to GitHub
```bash
cat ~/.ssh/id_rsa.pub
```
![SSH Key](image-19.png)  
![SSH Confirm](image-20.png)



### 🔹 Step 23: Clone Repository
```bash
git clone <your-repo-url>
```

---

## 💻 Final Configuration

### 🔹 Step 24: Set User Password
```bash
sudo passwd $(whoami)
```
Use `whoami` to find your username:  
![User Info](image-21.png)

### 🔹 Step 25: Enable Desktop Environment
```bash
echo "startxfce4" > ~/.xsession
cat ~/.xsession
startxfce4
sudo systemctl restart xrdp
sudo reboot
```

### 🔹 Step 26: Upload Service Key
Download from BigQuery and upload your **service key** into your project directory.

### 🔹 Step 27: Navigate to Ingestion Directory
```bash
cd /home/biscuit/NTU-Project-Data-Science-AI/ingestion_pipe
```

---

## 🎯 Run Dagster and Access UI

### 🔹 Step 28: Start Dagster
```bash
dagster dev
```
![alt text](image-25.png)

### 🔹 Step 29: Launch Windows RDP
Open Remote Desktop:  
![RDP](image-22.png)

### 🔹 Step 30: Enter IP Address
Use the external IP address from your VM configuration.

### 🔹 Step 31: Login
Enter your **Linux VM** username and password.

### 🔹 Step 32: Open Dagster UI in Chrome
```text
http://127.0.0.1:3000/
```
![Dagster UI](image-24.png)

---

✅ You’re all set! Dagster, Python, and DBT should now be running in your configured GCP environment!
