
<div align="center">

# ☁️ AWS Automation Dashboard

**Manage AWS resources through an interactive Python CLI dashboard.**

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/AWS-CLI-orange?style=for-the-badge&logo=amazonaws&logoColor=white">
<img src="https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge&logo=windows-terminal&logoColor=white">

</div>

---

## 📌 About

AWS Automation Dashboard is a menu-driven Python application that automates common AWS resource management operations using the AWS CLI.

It uses Python's `subprocess` module to execute AWS CLI commands, handle user input, and display command results directly in the terminal.

**No Boto3 is used in this project.**

## ✨ Features

| AWS Service | Operations |
|---|---|
| 🖥️ **EC2** | List, Launch, Start, Stop, Reboot and Terminate Instances |
| 🪣 **S3** | List, Create and Delete Buckets; List, Upload and Delete Objects |
| 🔐 **IAM** | List, Create and Delete Users; List and Create Roles; Attach and Detach Policies |
| ⚡ **Lambda** | List, Get, Create and Delete Functions |
| 🌐 **API Gateway** | API Gateway management operations |

## ⚙️ How It Works

<div align="center">

```text
       User Input
           │
           ▼
    Python Dashboard
           │
           ▼
    subprocess.run()
           │
           ▼
        AWS CLI
           │
           ▼
     AWS Services
    ┌──────┼──────┐
    ▼      ▼      ▼
   EC2     S3     IAM
                  │
             Lambda / API
              Gateway
```

</div>

## 🗂️ Project Structure

```text
AWS-CLI-Python-Dashboard/
│
├── main.py
│
├── services/
│   ├── ec2.py
│   ├── s3.py
│   ├── iam.py
│   ├── lambda_service.py
│   └── apigateway.py
│
├── core/
│   └── ...
│
├── logs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 🚀 Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

**2. Install prerequisites**

- Python 3.x
- AWS CLI
- An AWS account with the required IAM permissions

Verify installation:

```bash
python --version
aws --version
```

**3. Configure AWS CLI**

```bash
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, default region and output format.

Verify your AWS connection:

```bash
aws sts get-caller-identity
```

**4. Run the application**

```bash
python main.py
```

## 🖥️ Usage

1. Launch the application.
2. Select an AWS service from the main menu.
3. Choose the operation you want to perform.
4. Enter the required resource details.
5. View the AWS CLI response directly in the terminal.

## ⚠️ Important

- AWS credentials are configured locally and are not included in this repository.
- Each user must configure their own AWS CLI credentials.
- Required IAM permissions depend on the operations being performed.
- Some operations create billable AWS resources or permanently delete resources.

---

<div align="center">

**Built with Python 🐍 | Powered by AWS ☁️**

</div>
