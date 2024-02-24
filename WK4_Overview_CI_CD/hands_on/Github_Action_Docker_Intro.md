# i) Hands-on CD

## Step 1. Create a repo

1) Create a repo on Github UI and let us call it `docker-intro`, 

2) Add a README file and make sure the MAIN branch is available

3) Git clone this repo to your local repo


## Step 2. Commit your code as a developer

1) Check out a new branch `git checkout -b "issue/MP-1-init-the-folder"`
2) Copy file `Dockerfile` and folder `src/` over from `WK3_Dockerisation/docker-intro`
3) Add the files and folders `git add .`
4) Commit `git commit -m "MP-1 Initialise the folder"`
5) Git push `git push --set-upstream origin issue/MP-1-init-the-folder`
6) Create a Pull Request and Merge the Pull Request
7) `git checkout MAIN & git pull`


## Step 3. Create an application on Elastic beanstalk

Create an Elastic beanstalk application on `ap-southeast-2` (Sydney). Let us name it `sample-docker-react`.

Elastic beanstalk will create an environment for us called `Sample-docker-react-env`

Choose Docker as the engine and sample application code and submit


## Step 4. Create IAM user

In IAM -> users, create a user, attach policy with 
* AdministratorElasticBeanstalk
* EC2FullAccess
* VPCFullAccess


## Step 5. Create Access Credentials and set up github action
Once the user is created, click on security credentials -> access credentials -> create access

Choose the first option `using AWS cli to access AWS services` and note down the credentials (download the .csv file)

And then go to your git repo -> Settings -> Secrets and variables -> Actions -> New Repository Secrets add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY respectively with their values.


## Step 6. Create another PR to add a CD yml file
1) Create another branch
2) Create a folder `mkdir -p .github/workflows/` and a yaml file`touch .github/workflows/cd-elasticbeanstalk.yml`
3) Check the S3 bucket name and note it down
4) Update the S3 bucket name in the script below. 
5) Commit, push, review and merge PR

(Note if you did not use ap-southeast-2 (Sydney) region, you need to update the field in the script as well) 

```
name: Deploy to Elastic Beanstalk

on:
  pull_request:
    types: [closed]
  workflow_dispatch:


jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Create ZIP deployment package
        run: zip -r deploy_package.zip ./  

      - name: Install AWS CLI
        run: |
          sudo apt-get update
          sudo apt-get install -y python3-pip
          pip3 install --user awscli

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v1
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ap-southeast-2

      - name: Upload package to S3 bucket
        run: aws s3 cp deploy_package.zip s3://elasticbeanstalk-ap-southeast-2-482739392776

      - name: Deploy to Elastic Beanstalk
        run: |
          aws elasticbeanstalk create-application-version \
            --application-name sample-docker-react \
            --version-label ${{ github.sha }} \
            --source-bundle S3Bucket="elasticbeanstalk-ap-southeast-2-482739392776",S3Key="deploy_package.zip"
          
          aws elasticbeanstalk update-environment \
            --environment-name Sample-docker-react-env \
            --version-label ${{ github.sha }}
```

## Step 7 Viola

The deployment will now be triggered everytime you merge a PR.
