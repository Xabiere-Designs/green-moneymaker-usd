#!/bin/bash
# This is a shebang line that specifies the interpreter for the script as "/bin/bash".

# Update the package list for APT package manager with the "-y" flag for automatic "yes" responses.
sudo apt-get update -y

# Fetch the Jenkins GPG key and store it in /usr/share/keyrings/jenkins-keyring.asc
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

# Add the Jenkins repository to the APT sources list with the GPG key.
# This line adds the repository and specifies the location of the keyring.
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

# Update the package list again to include the Jenkins repository.
sudo apt-get update -y

# Install Jenkins using APT package manager with the "-y" flag for automatic "yes" responses.
sudo apt-get install jenkins -y

# Update the package list for APT again.
sudo apt update

# Install the "fontconfig" and "openjdk-17-jre" packages using APT with automatic "yes" responses.
sudo apt install fontconfig openjdk-17-jre -y

# Enable the Jenkins service to start on boot.
sudo systemctl enable jenkins

# Start the Jenkins service.
sudo systemctl start jenkins



