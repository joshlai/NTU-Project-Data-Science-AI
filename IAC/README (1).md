# VM Setup and Environment Initialization Guide

This guide provides step-by-step instructions to spin up a GCP VM instance with **2 vCPUs, 10GB HDD**, and **4GB RAM**. This setup is ideal for running **Dagster**, **Python**, and **DBT**.  


> ⚠️ **Note:** Ensure your project uses the exact same file structure to avoid issues.

---

## Step-by-Step Instructions

### Step 1  
In the GCP Console, search for **Compute**:  
![alt text](image.png)

### Step 2  
Select **Compute Engine**:  
![alt text](image-1.png)

### Step 3  
You will arrive at the Compute Engine dashboard:  
![alt text](image-2.png)

### Step 4  
Click on the **Google Cloud Shell** icon at the top right:  
![alt text](image-3.png)

### Step 5  
Cloud Shell is launched:  
![alt text](image-4.png)

### Step 6  
Upload the `create-vm.sh` script (from the `IAC` folder) into the terminal:  
![alt text](image-5.png)

### Step 7  
Use `ls` to verify upload. The file should appear in white (non-executable):  
![alt text](image-6.png)

### Step 8  
Make the file executable:
```bash
chmod +x create-vm.sh
ls
```
If successful, the file will turn green:  
![alt text](image-7.png)

### Step 9  
Run the script:
```bash
./create-vm.sh
```
Ignore disk size warning:  
![alt text](image-8.png)

### Step 10  
Click **VM Instances** to refresh the VM console:  
![alt text](image-9.png)

### Step 11  
You should now see a VM named `vm-etl-2`:  
![alt text](image-10.png)

### Step 12 *(Optional)*  
If not proceeding immediately, stop the VM to avoid incurring charges:  
![alt text](image-11.png)

### Step 13  
Click on the created VM:  
![alt text](image-12.png)

### Step 14  
Click **SSH** and allow authorization:  
![alt text](image-15.png)

### Step 15  
Check working directory and create a new folder:
```bash
cd ~
mkdir biscuit
cd biscuit
```
![alt text](image-13.png)

### Step 16  
Upload `environment.yml` and `setup.sh`. Make the script executable and run:
```bash
chmod +x setup.sh
./setup.sh
```
![alt text](image-16.png)

### Step 17  
Select both services for restart:  
![alt text](image-17.png)

### Step 18  
Choose **lightdm** and reboot when prompted.

---

### Step 19  
Create the Conda environment:
```bash
conda env create -f environment.yml
```

### Step 20  
Activate the environment:
```bash
conda activate <your_env_name>
```

### Step 21  
Generate SSH key:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Press Enter 3 times to accept defaults.  
![alt text](image-19.png)  
![alt text](image-20.png)

### Step 22  
Copy your public key to GitHub:
```bash
cat ~/.ssh/id_rsa.pub
```

### Step 23  
Clone your GitHub repo:
```bash
git clone <your-repo-url>
```

### Step 24  
Set a user password:
```bash
sudo passwd $(whoami)
```
Use `whoami` to find your username:  
![alt text](image-21.png)

### Step 25  
Enable desktop environment:
```bash
echo "startxfce4" > ~/.xsession
cat ~/.xsession
startxfce4
sudo systemctl restart xrdp
sudo reboot
```

### Step 26  
Download from big query your service key and upload the **service key** into your project directory.

### Step 27  
Navigate to your project ingestion directory:

```bash
cd /home/biscuit/NTU-Project-Data-Science-AI/ingestion_pipe
```

### Step 28  
Start Dagster:
```bash
dagster dev
```
![alt text](image-23.png)

![alt text](image-22.png)
### Step 29  
Launch **Windows Remote Desktop (RDP)**:  


### Step 30  
Enter the external IP address from the GCP VM settings.

### Step 31  
Login with your Linux VM username and password.

### Step 32  
Launch Chrome and open Dagster UI:
```text
http://127.0.0.1:3000/
```
![alt text](image-24.png)
