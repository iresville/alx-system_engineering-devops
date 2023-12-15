#!/usr/bin/env bash
# This script installs MySQL 5.7 on a server

# Add the MySQL GPG Key
echo "Adding MySQL GPG Key..."
wget https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html -O signature.key
sudo apt-key add signature.key

# Add the MySQL Repository
echo "Adding MySQL Repository..."
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

# Update the package list
echo "Updating package list..."
sudo apt-get update

# Install MySQL 5.7
echo "Installing MySQL 5.7..."
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

# Verify MySQL version
echo "Verifying MySQL version..."
mysql_version=$(mysql --version)
echo $mysql_version

# Check if the version is correct
if [[ $mysql_version == *"5.7."* ]]; then
    echo "MySQL 5.7 installed successfully!"
else
    echo "Failed to install MySQL 5.7"
    exit 1
fi
