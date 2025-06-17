#Introduction
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









Step 14 









