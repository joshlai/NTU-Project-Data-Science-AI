# Introduction
By Following the instructions stated below, users will be able to spin up an ec2 vm with 2 vCPUs , 10gb HDD and 4GB of ram which is useful for running Dagster, Python and DBT.After spinningup the VM please follow environment.md to create an environment for running the necessary libraries.





Step1
In the search bar of the GCP Console, type Compute


![alt text](image.png)

Step 2 Select the Compute Engine


![alt text](image-1.png)

Step 3 You will arrive at the compute console






![alt text](image-2.png)

Step 4 Select the Google Cloud Console It is at the top right


![alt text](image-3.png)


Step 5 Cloud Shell Is launched



![alt text](image-4.png)

Step 7 Upload the "create-vm.sh" via the cloud console into the terminal. The file is located in IAC folder. See screen shot above.


![alt text](image-5.png)

Step 8 use the "ls" command to check if the file has been uploaded. The file should be in while colour. The file needs to made into an executable. See the image above


![alt text](image-6.png)

Step 9 Run the command  "chmod +x create-vm.sh" followed by the ls command . If run correctly the create-vm.sh will now be a green colour.See the image above.






![alt text](image-7.png)
Step 10 
run "./create-vm.sh" in the Cloud Shell.Ignore the disk size warning. There is no impact to the run speed.



![alt text](image-8.png)

Step 11 Click on the VM Instances to refresh the VM console. 




![alt text](image-9.png)

Step 12
You will now see virtual machine named vm-etl-2.

![alt text](image-10.png)



Step 13 -optional if you are not proceeding to install the environment. Click on the 3 dots and Click Stop VM. Failure to do so will incur running costs!.





![alt text](image-11.png)
Step 14- Click On the created VM as shown 

![alt text](image-12.png)
Step 15- Clock on the SSH Connection. When Prompted , Allow Authorization




![alt text](image-15.png)
Step 16- Check workign directory and use the cd command to goto the home directory. Use the command "mkdir biscuit" to create a new directory. cd into the newly created directory.




![alt text](image-13.png)
Step 16- Click on the upload files. Upload the "environment.yml" and the "setup.sh"  Copy it to the newly created biscuit directory. Make the script executable "chmod +x setup.sh" Run the script.




![alt text](image-16.png)
Step 17 Select Both Services to be restarted


![alt text](image-17.png)
Step 18 Choose lightdm. Follow the instructions on screen to reboot when done.


Step 19
Use the command "conda env create -f environment.yml" to install all the neccessary packages

Step 20
Activate the conda environment created

Step 21
a)Use the command below to create the ssh key to link to git hub
b)ssh-keygen -t ed25519 -C "your_email@example.com"
c)enter x 3 to accept the file location and to get teh defaults


![alt text](image-19.png)
![alt text](image-20.png)
Step 22
Run.
cat ~/.ssh/id_rsa.pub  Parts have been redacte. The key is quite long. Copy and paste this into Git hub.




Step 24
Git Clone the repo from Git Hub


Step 25
use the following command to create password
sudo passwd your user id


![alt text](image-21.png)




Step 26
echo "startxfce4" > ~/.xsession
cat ~/.xsession
startxfce4
sudo systemctl restart xrdp
sudo reboot































