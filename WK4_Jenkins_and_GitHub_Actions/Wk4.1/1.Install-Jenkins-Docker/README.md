# Jenkins Basic

## About Jenkins

Jenkins is a powerful application that allows continuous integration and continuous delivery of projects, regardless of the platform you are working on. It's a popular tool for performing continuous integration of software projects.

![Alt text](images/why_jenkins.jpg?raw=true)

Jenkins is a free source that can handle any kind of automated build or continuous integration. You can integrate Jenkins with a number of testing and deployment technologies.

## About CI/CD

First of all, let's review the advantages of continuous integration:

1. reduce the labor force
2. avoid human error
3. improve efficiency
4. continuous feedback on quality
5. quality assurance

Second, to use Jenkins for continuously integration, you should have knowledge including:

* Linux
* Git
* Jenkins
* Maven
* JDK
* Other programming tools

### Continuous Integration

Continuous Integration (CI) helps developers integrate code into a shared repository by automatically verifying the build using unit tests and packaging the solution each time new code changes are submitted.

For example, setting up a CI pipeline for Continuous Integration with a SharePoint Framework solution requires the following steps:

1. Creating the Build Definition
2. Installing NodeJS
3. Restoring dependencies
4. Executing Unit Tests
5. Importing test results
6. Importing code coverage information
7. Bundling the solution
8. Packaging the solution
9. Preparing the artifacts
10. Publishing the artifacts

![Alt text](images/jenkins_ci.webp?raw=true)

### Continuous Deployment

Continuous Deployment (CD) takes validated code packages from build process and deploys them into a staging or production environment. Developers can track which deployments were successful or not and narrow down issues to specific package versions.

Setting up a CD pipeline for Continuous Deployments with a SharePoint Framework solution requires the following steps:

1. Creating the Release Definition
2. Linking the Build Artifact
3. Creating the Environment
4. Installing NodeJS
5. Installing the CLI for Microsoft 365
6. Connecting to the App Catalog
7. Adding the Solution Package to the App Catalog
8. Deploying the Application
9. Setting the Variables for the Environment

![Alt text](images/jenkins_cd.webp?raw=true)

### CI/CD with third-party solutions/services

You can also use the Jenkins open-source automation server to deploy AWS CodeBuild artifacts with AWS CodeDeploy, creating a functioning CI/CD pipeline. When properly implemented, the CI/CD pipeline is triggered by code changes pushed to your GitHub repo, automatically fed into CodeBuild, then the output is deployed on CodeDeploy.

![Alt text](images/jenkins_aws_cicd.png?raw=true)

## Install Jenkins on Docker

This is to guide how to install Jenkins and run it in a Docker container.

### Pre-requisite

* Software: Docker

### Steps

#### 1. Create a folder to hold Jenkins data

```bash
mkdir jenkins_home
cd jenkins_home
```

#### 2. Start a Jenkins container

```bash
docker run --name jenkins \
           -u root \
           -d \
           -v $(pwd):/var/jenkins_home \
           -v /var/run/docker.sock:/var/run/docker.sock \
           -p 80:8080 \
           -p 50000:50000 \
           jenkins/jenkins:lts-jdk11
```

> Note:
>
> * `-u root` configures to run Jenkins by root user.
> * `-d` detaches the container
> * `-v $(pwd):/var/jenkins_home` mounts the current directory to Jenkins home inside the container
> * `-v /var/run/docker.sock:/var/run/docker.sock` mounts Docker socks
> * `-p 80:8080` maps port 80 in the host to port 8080 inside the container
> * `-p 50000:50000` maps ports 50000 which is the default port for angent registration
> * `jenkins/jenkins:lts-jdk11` is the image maintained by `jenkin`.
> * If you have error with port 80, please change it to 8080 or other port numbers.

#### 3. Open <http://127.0.0.1> and you should see screen below

![Alt text](images/docker-install-01.png?raw=true)

#### 4. Get your password by opening `secrets/initialAdminPassword` file in the directory you created in the first step

```bash
sudo cat secrets/initialAdminPassword
```
You can also get the initial password from your Docker container log, or you can bash into your Docker container and get it from inside:

To see the docker container id

```bash
docker container ls 
```
Then enter in bash inside a container.

```bash
docker exec -it CONTAINER_ID bash
```

#### 5. Continue installation in step #3 with password from step #4

You should see screen below after full installation.
![Alt text](images/docker-install-02.png?raw=true)
