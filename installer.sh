#!/bin/bash

# This script installs the Ransomware Recovery Tool dependencies and sets up the environment on a Linux system (Debian or Red-Hat based).

# Update package list and install required packages (after checking distribution type)
if [ -f /etc/debian_version ]; then
    echo "Detected Debian-based system. Updating package list and installing dependencies..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip git
elif [ -f /etc/redhat-release ]; then
    echo "Detected Red Hat-based system. Updating package list and installing dependencies..."
    sudo dnf update -y
    sudo dnf install -y python3 python3-pip git
else
    echo "Unsupported Linux distribution. Please install Python 3, pip, and git manually."
    exit 1
fi  


# Clone the repository
echo "Cloning the Ransomware Recovery Tool repository..."
git clone https://github.com/flo7716/Ransomware_recovery_tool
cd Ransomware_recovery_tool



# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt


# Make the script executable
chmod +x core/decryptors/*.py

# Create a symbolic link for the main script
echo "Creating symbolic link for the main script..."
sudo ln -s "$(pwd)/core/decryptors/main.py" /usr/local/bin/ransomware_recovery_tool

# Print completion message
echo "Installation complete! You can now run the Ransomware Recovery Tool using the command 'ransomware_recovery_tool'."
echo "For help, use 'ransomware_recovery_tool --help'."

