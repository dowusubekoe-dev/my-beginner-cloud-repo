#### Pre-requisites
- Create an IAM User and check the box for Access Key and Password AWS Management Console access
- Click Next:Permission
- Create a Group and select group policy "AdministratorAccess"
- Provide the tag/key and go to next
- Review and create user
- Copy and save the AccessKey ID and Secret Key ID or download the spreadsheet file

1. Create a Windows EC2 Instance and generate the RDP file for remote desktop connection
2. Configure an EC2 Windows instance to allow file downloads using Internet Explorer
    - Settings->Internet Options->Security->Custom level->Scroll to Downloads
    - Enable->Ok->Apply
3. Installing AWS CLI On Windows EC2 Instance
    - Download the AWS CLI installer for Windows (64-bit) and click on save. https://awscli.amazonaws.com/AWSCLIV2.msi
    - Go through the defaults to complete the installation
    - Check the version [aws --version]

4. Configuring AWS CLI
    - To configure the installation, run [aws configure] then Enter
    - Copy the AWS Access Key ID for the IAM User and paste in the command prompt
    - Copy the AWS Secret Access Key for the IAM User and paste in the command prompt
    - Provide the region
    - Type in the default format as [json]

    ###### Creating and Deleting Bucket Using AWS CLI
    $ aws s3 mb s3://uniquebucketname
    $ aws s3 ls

    - Verify from the AWS console if the S3 bucket has been created

    $ aws s3 rb s3://uniquebucketname
    $ aws s3 ls
    $ aws ec2 describe-instances


5. Installing Git
    - Open your browser and click on the link to download Git https://git-scm.com/download/win
    - Go through the defaults to complete the installation

6. Installing Node.js
    - Click on the link https://nodejs.org/en/
    - Download the node-xx.xx.0-x64.msi version
    - Run and install the downloaded Node version

7. Setting up AWS SDK
    - Download a sample project Run command in command line
    $ git clone https://github.com/aws-samples/aws-nodejs-sample.git
    - Install SDK Dependencies
    $ cd aws-nodejs-sample
    $ npm install
    - Run sample SDK program
    $ node sample.js