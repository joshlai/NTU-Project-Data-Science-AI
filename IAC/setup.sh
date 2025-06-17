#!/bin/bash

# Exit if any command fails
set -e

echo "📦 Step 1: Updating system packages..."
sudo apt update && sudo apt upgrade -y
echo "✅ System update completed."

echo "🐙 Step 2: Installing Git..."
sudo apt install -y git
echo "✅ Git installed."

echo "📥 Step 3: Downloading Miniconda installer..."
MINICONDA=Miniconda3-latest-Linux-x86_64.sh
wget https://repo.anaconda.com/miniconda/$MINICONDA -O /tmp/$MINICONDA

echo "📦 Step 4: Installing Miniconda..."
bash /tmp/$MINICONDA -b -p $HOME/miniconda

echo "🔧 Step 5: Adding Miniconda to PATH..."
echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> ~/.bashrc

echo "🔄 Step 6: Initializing Conda for bash shell..."
$HOME/miniconda/bin/conda init bash

echo "🖥️ Step 7: Installing lightweight XFCE desktop (Xubuntu core)..."
sudo apt install -y xubuntu-core

echo "🖥️ Step 8: Installing LightDM display manager..."
sudo apt install -y lightdm
sudo systemctl enable lightdm

echo "🔐 Step 9: Installing RDP support with xrdp..."
sudo apt install -y xrdp
sudo systemctl enable xrdp

echo "🌐 Step 10: Installing Google Chrome..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/chrome.deb
sudo apt install -y /tmp/chrome.deb || sudo apt --fix-broken install -y
echo "✅ Google Chrome installed."

echo "✅ All installations complete!"
echo "Please restart your terminal or run:"
echo "   source ~/.bashrc"
echo "You may reboot the machine to start the GUI with:"
echo "   sudo reboot"
