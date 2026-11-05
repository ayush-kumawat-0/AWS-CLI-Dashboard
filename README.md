 <div align="center">

# ☁️ AWS Automation Dashboard

**Manage AWS resources through a Python-powered CLI dashboard.**

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/AWS-CLI-orange?style=for-the-badge&logo=amazonaws&logoColor=white" />
<img src="https://img.shields.io/badge/Interface-CLI-black?style=for-the-badge&logo=windows-terminal&logoColor=white" />

</div>

---

## 📌 About the Project

AWS Automation Dashboard is a menu-driven Python application designed to simplify AWS resource management using the AWS CLI.

It uses Python's `subprocess` module to execute AWS CLI commands, collect user input, handle command responses, and display results directly in the terminal.

**Technology:** Python + AWS CLI (No Boto3).

## ✨ Features

| AWS Service | Operations |
|---|---|
| 🖥️ **EC2** | List, Launch, Start, Stop, Reboot and Terminate Instances |
| 🪣 **S3** | List, Create and Delete Buckets; List, Upload and Delete Objects |
| 🔐 **IAM** | List, Create and Delete Users; List and Create Roles; Attach and Detach Policies |
| ⚡ **Lambda** | List, Get, Create and Delete Functions |
| 🌐 **API Gateway** | API Gateway management through the dedicated service module |

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
       ┌──────┼───────┐
       ▼      ▼       ▼
      EC2     S3      IAM
                      │
                 Lambda / API
                   Gateway
```

</div>

## 🗂️ Project Structure

```text
AWS-CLI-Python-Dashboard/
│
├── core/
│   ├── __pycache__/
│   └── aws_cli.py
│
├── services/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── apigateway.py
│   ├── ec2.py
│   ├── iam.py
│   ├── lambda_service.py
│   ├── modified_ec2.py
│   └── s3.py
│
├── main.py
├── README.md
└── requirements.txt
```

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.x
- AWS CLI
- AWS account
- Appropriate IAM permissions

Check installation:

```bash
python --version
aws --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

cd AWS-CLI-Python-Dashboard
```

### 3. Configure AWS CLI

```bash
aws configure
```

Enter your:

- AWS Access Key ID
- AWS Secret Access Key
- Default region
- Default output format

Verify your AWS connection:

```bash
aws sts get-caller-identity
```

### 4. Run the Dashboard

```bash
python main.py
```

## 🖥️ Usage

1. Run `main.py` to launch the dashboard.
2. Select an AWS service from the main menu.
3. Choose the required operation.
4. Enter the requested resource details.
5. View the command output or error directly in the terminal.

## ⚠️ Important

- Every user must configure their own AWS credentials.
- AWS credentials are not included in this repository.
- Required IAM permissions depend on the selected operation.
- Some AWS operations may create billable resources or permanently delete existing resources.

---

<div align="center">

**Built with Python 🐍 | Powered by AWS ☁️**

</div>