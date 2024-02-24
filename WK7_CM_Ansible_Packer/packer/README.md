# Description
This demos the most common usage of packer - build AMI (Amazon Machine Image)

# Pre-requisite:
## Install packer

https://www.packer.io/docs/install


# Tasks

# Task 1: Build AMIs
## build simple AMI - 1.bake-ec2-to-image-shell-provisioner
This demos a basic AMI creation by packer using shell provisioner.
Please make sure your ssh key and AWS credentials are configured.
```
export AWS_ACCESS_KEY_ID="xxxx"
export AWS_SECRET_ACCESS_KEY="xxxx"
cd 1.bake-ec2-to-image-shell-provisioner
packer init .
packer fmt .
packer validate .
packer build aws-shell.pkr.hcl
```

## build AMI provisioned by ansible - 2.bake-ec2-to-image-ansible-provisioner
This demos an AMI creation by packer using ansible provisioner.
```
cd 2.bake-ec2-to-image-ansible-provisioner
packer build aws-ansible.pkr.hcl
```

# Task 2: Use AMI
## Launch an EC2 instance by AMI - AWS Console
Please exercise this in AWS EC2 console. Select the AMI that we built. Verify that EC2 instance has the changes
 - /home/ubuntu/hello.txt
 - nginx installed

## Launch an EC2 instance by AMI - Terraform or Cloudformation
Use Terraform or Cloudformation to create an EC2 instance by our AMI.
 - Configure "User Data" of EC2 instance to start up docker container during system start or use "Systemd" to do that.

For example

```
#!/bin/bash
systemctl start nginx.service
systemctl enable nginx.service
cat <<EOF > /var/www/html/index.html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to Jiangren Devops!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to Jiangren Devops!</h1>
<p>Hello from $(hostname -f)</p>
</body>
</html>
EOF
```

# Reference

[Packer tutorial - AWS](https://learn.hashicorp.com/tutorials/packer/get-started-install-cli?in=packer/aws-get-started)