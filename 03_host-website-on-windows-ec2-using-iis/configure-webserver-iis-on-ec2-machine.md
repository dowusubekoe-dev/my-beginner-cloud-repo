
### Creating Windows Machine On AWS
1. Search for EC2 in the AWS Management Console.
2. Give the EC2 instance a unique name. Eg. *demoWindowsInstance*
3. Select an AMI (Amazon Machine Image) Eg. *Microsoft Windows Server 2022 Base*
4. Select the instance type. Eg. *t2.micro*
5. Create a Key Pair. **AWS provides the Public Key and the Customer need to store the Private Key**
	- Click on Create key pair.
	- Provide a name for the Key pair. Eg. *windowsInstanceKeyPair*
    - Select the radio button for *.pem* when using SSH and *.ppk* for Putty https://putty.org/
    - Click on *Create key pair* and download to root folder of your project.
    **Do not store any Key pair, access key or password in your GitHub project folder or your will receive a security email from Amazon**
6. Amazon automatically creates Default VPC and Security Group if you do not prefer setting up your own.
7. Check the box for **Allow RDP traffic from Anywhere** *Helps you connect to your instance*
8. Configure storage by selecting another storage type or use the default selected by Amazon.
9. Verify the number of instances you want to create.
10. Click on *Launch instance*
11. Click on *View all instances* and wait for all **Status checks** to be completed.

### Connecting to the created Windows instance
1. Select the instance by checking off the box.
2. Click on **Connect** button
3. From the *Connect to instance* tab, click on the *RDP client* and select *Connect using RDP client*
4. Click on **Download remote desktop file** to download the your project folder.

### Getting the Password
1. Click on *Get password*
2. Click on *Upload private key file* and select the public key (*windowsInstanceKeyPair.pem*) you saved earlier and upload.
3. Click on *Decrypt password*
4. Copy the generated password and save it for later use.

### Remote Desktop Connection to the Windows Instance from a Mac
1. For Mac users, download and install Microsoft Remote Desktop https://apps.apple.com/au/app/microsoft-remote-desktop/id1295203466?mt=12 and for Windows users, download using this link https://apps.microsoft.com/store/detail/microsoft-remote-desktop/9WZDNCRFJ3PS?hl=en-us&gl=us
2. For Mac users, copy the Public IP address of the instance and configure it on the Microsoft Remote Desktop app
3. From the Microsoft Remote Desktop app, click on the + sign and paste the Public IP address. Save and right click the pc and select **Connect**
4. For Windows users, right click on the downloaded Remote Desktop file and open with *Remote Desktop Connection*

### Change Windows Password
- Go to **Control Panel** -—> **User Account** -—> **User Account** -—> **Manage Account** -—> **Change Account** -—> **Change Password**
- Enter old password (the one decrypted from AWS)
- Type in the new password

### Internet Explorer Settings
- Launch IE
- Go to **Settings** --> **Internet Options** --> **Security tab** --> **Custom level**
- Search for "Download" and "Enable"
- Save changes and click on **Apply**

### Install the AWSCLI
- Go to https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- Download the AWS CLI based on the operating system you are using

For Linux x86 (64-bit)
    ```curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install```

For MacOS
    In your browser, download the macOS pkg file: https://awscli.amazonaws.com/AWSCLIV2.pkg

For Windows
    Download and run the AWS CLI MSI installer for Windows (64-bit): https://awscli.amazonaws.com/AWSCLIV2.msi
    Alternatively, you can run the msiexec command to run the MSI installer. C:\> msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi

### Install IIS
- Launch the server manager tool
- Go to **Add roles and features** then click Next
- Select radio button for **Role-based or feature-based installation**, then Next
- Next
- Under *Server Roles* check the box for **Web Server (IIS)**, then Next
- Click on *Add Features* and then Next
- Click on **Install**

