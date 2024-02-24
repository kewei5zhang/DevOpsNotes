# Installation on Ubuntu

## Prerequisites

A physical/virtual machine meeting with minimum hardware requirements:

* **256 MB** of RAM

* **1 GB** of drive space (although **10 GB** is a recommended minimum if running Jenkins as a Docker container)

Recommended hardware configuration for a small team:

* **4 GB+** of RAM

* **50 GB+** of drive space

Comprehensive hardware recommendations:

* Hardware: see the [Hardware Recommendations](https://www.jenkins.io/doc/book/scaling/hardware-recommendations) page

> NOTE: Before proceeding with this tutorial, make sure that you are logged in as a user with sudo privileges.

To install Jenkins on an Ubuntu system, perform the following steps:

### Installation of Java

Since Jenkins is a Java application, the first step is to install Java.

There are multiple Java implementations which you can use. OpenJDK is the most popular one at the moment, we will use it in this guide.

Update the package index and install the  Open Java Development Kit (OpenJDK) package using the following command:

```bash
sudo apt update
sudo apt install openjdk-11-jdk
```

You need to hit **``Y``** to confirm and continue.

If you have more than one java version installed on your computer, make sure your default Java package version is supported by Jenkins.

## Add apt repository

Jenkins has two release for Ubuntu: **LTS (Long-Term Support) release** and **Weekly release**. Both can be installed through ``apt``.

**A LTS (Long-Term Support) release** is chosen every 12 weeks from the stream of regular releases as the stable release for that time period. It can be installed from the ``debian-stable apt`` [repository](https://pkg.jenkins.io/debian-stable/).

**Weekly release** is produced weekly to deliver bug fixes and features to users and plugin developers. It can be installed from the ``debian apt`` [repository](https://pkg.jenkins.io/debian/).

You need to add the Jenkins Debian repository to your local apt list.

First, use the following ``wget`` command to import the GPG key for the Jenkins repository:

```bash
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo apt-key add -
```

The output of above command should be **``OK``**, which means that the key was successfully imported and that packages from this repository will be considered trusted.

Next, add the Jenkins repository to the system using the following command:

```bash
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
```

There is no output from above command.

## Install Jenkins

Once the Jenkins repository is added and enabled, you can update the package list and install the latest version of Jenkins by typing: ``apt``

```bash
sudo apt update
```

From the output you should see the package lists read from jenkins.io.

```bash
[Output]
...
Ign:4 https://pkg.jenkins.io/debian-stable binary/ InRelease
Get:6 https://pkg.jenkins.io/debian-stable binary/ Release [2044 B]
Get:7 https://pkg.jenkins.io/debian-stable binary/ Release.gpg [833 B]
Get:8 https://pkg.jenkins.io/debian-stable binary/ Packages [21.2 kB]
...
```

Now, let's install it. Don't forget to hit **``Y``** to confirm:

```bash
sudo apt install jenkins
```

The Jenkins service will start automatically after the installation is complete. You can verify the service status:

```bash
systemctl status jenkins
```

You should see something like this:

```bash
● jenkins.service - LSB: Start Jenkins at boot time
     Loaded: loaded (/etc/init.d/jenkins; generated)
     Active: active (exited) since Wed 2022-02-02 05:08:56 UTC; 1min 3s ago
       Docs: man:systemd-sysv-generator(8)
      Tasks: 0 (limit: 38522)
     Memory: 0B
     CGroup: /system.slice/jenkins.service

Feb 02 05:08:55 jenkins-ubuntu systemd[1]: Starting LSB: Start Jenkins at boot time...
Feb 02 05:08:55 jenkins-ubuntu jenkins[7934]: Correct java version found
Feb 02 05:08:55 jenkins-ubuntu jenkins[7934]:  * Starting Jenkins Automation Server jenkins
Feb 02 05:08:55 jenkins-ubuntu su[7973]: (to jenkins) root on none
Feb 02 05:08:55 jenkins-ubuntu su[7973]: pam_unix(su-l:session): session opened for user jenkins by (uid=0)
Feb 02 05:08:55 jenkins-ubuntu su[7973]: pam_unix(su-l:session): session closed for user jenkins
Feb 02 05:08:56 jenkins-ubuntu jenkins[7934]:    ...done.
Feb 02 05:08:56 jenkins-ubuntu systemd[1]: Started LSB: Start Jenkins at boot time.
```

## Update the Firewall Configuration

If your Jenkins is installed on a remote Ubuntu server and protected by OS firewall, you need to allow the inbound traffic to port ``8080`` so you can access Jenkins server from Web browser.

Assuming your Ubuntu uses ``UFW`` firewall  management, you can allow the port with the following command:

```bash
sudo ufw allow 8080
```

Outputs should be like:

```bash
Rules updated
Rules updated (v6)
```

Verify the changes by:

```bash
sudo ufw status

Status: active

To                         Action      From
--                         ------      ----
8080                       ALLOW       Anywhere
22                         ALLOW       Anywhere
8080 (v6)                  ALLOW       Anywhere (v6)
22 (v6)                    ALLOW       Anywhere (v6)
```

## Azure Network Security Group Setting

By default you will have Azure NSG to protect your network connections to and from your VM. The NSG is a white/black list to allow or deny some traffic by rules.

To secure your VM, please set up the NSG rules as below:

![Alt text](images/az-nsg.png)

## Jenkins Setup

Continue in a Web browser to complete the new Jenkins installation. Type your domain or IP address in address bar, then type port ``http://<your_ip_or_hostname>:8080``, and then a screen similar to the following will appear:

![Alt text](images/jenkins_web_install.png?raw=true)

The Jenkins installer creates an initial 32-character alphanumeric Administrator password. Before getting started, you need to use the following command to get the password from your terminal to unlock Jenkins server:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

0000173xxxxf4e99xxxxxe99a87xxxxx
```

Copy the password from your terminal, paste it into the administrator password field, and click ``Continue``.

On the next screen, the setup wizard will ask if you want to install the recommended plugin or if you want to select a specific plugin.

![Alt text](images/jenkins_web_install_plugin.png?raw=true)

Click on the box ``Install suggested plugins`` and the installation process will begin immediately.

![Alt text](images/jenkins_web_install_plugin_installing.png?raw=true)

After the plug-in is installed, you will be prompted to set up your first admin user. fill in all the required information, and then click ``Save and Continue``.

![Alt text](images/jenkins_web_install_create_admin.png?raw=true)

> NOTE: You can also skip this step to continue with Admin user. However, this is not recommended.

The next page will ask you to set the URL of the Jenkins instance. The field will be populated with the auto-generated URL.

> NOTE: Please keep this URL as we will use it later for tools integration.

Then confirm the URL by clicking the ``Save and Finish`` button and the setup will be completed.

Then click on the ``Start using Jenkins`` button and you will be redirected to the **Jenkins dashboard** logged in as the admin user you created in one of the previous steps.

![Alt text](images/jenkins_web_welcome.png?raw=true)

At this point, you have successfully installed Jenkins on your Ubuntu system.
