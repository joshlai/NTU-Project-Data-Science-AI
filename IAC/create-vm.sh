#!/bin/bash

# ---- CONFIGURABLE ----
VM_NAME="vm-elt-2"
ZONE="us-central1-b"
MACHINE_TYPE="e2-highcpu-8"
IMAGE_FAMILY="ubuntu-2204-lts"
IMAGE_PROJECT="ubuntu-os-cloud"
DISK_SIZE="20GB"

# ---- EXECUTE ----
echo "Creating VM: $VM_NAME in $ZONE..."

gcloud compute instances create $VM_NAME \
  --zone=$ZONE \
  --machine-type=$MACHINE_TYPE \
  --image-family=$IMAGE_FAMILY \
  --image-project=$IMAGE_PROJECT \
  --boot-disk-size=$DISK_SIZE \
  --boot-disk-type=pd-standard \
  --tags=http-server,https-server \
  --metadata=startup-script='#!/bin/bash
    sudo apt update
    sudo apt install -y nginx' \
  --scopes=https://www.googleapis.com/auth/cloud-platform

echo "✅ VM $VM_NAME created successfully."
