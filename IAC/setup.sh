#!/bin/bash

#quit if any of the commands below fails
set -e
echo "Proceeding to update system packages for ubuntu"

sudo apt update && sudo apt upgrade -y

echo "Update for Ubuntu completed"

echo "Proceeeding to install Git"
sudo apt install -y git

echo "Downloading Miniconda installer"
MINICONDA=Miniconda3-latest-Linux-x86_64.sh
wget https://repo.anaconda.com/miniconda/$MINICONDA -O /tmp/$MINICONDA


echo "installing Miniconda"
bash /tmp/$MINICONDA -b -p $HOME/miniconda


## Add conda to PATH
echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

##Optional : initialize conda for bash shell
$HOME/miniconda/bin/conda init bash


echo "installation complete, please restart your shell"


