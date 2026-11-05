
<div align="center">

# ☁️ AWS Automation Dashboard

### Manage AWS resources directly from your terminal using Python and the AWS CLI.

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/AWS-CLI-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">
  <img src="https://img.shields.io/badge/Interface-CLI-00A67D?style=for-the-badge&logo=windows-terminal&logoColor=white">
  <img src="https://img.shields.io/badge/Status-Learning%20Project-orange?style=for-the-badge">
</p>

**A menu-driven Python project for automating common AWS operations.**

[Features](#-features) · [Architecture](#-how-it-works) · [Setup](#-getting-started) · [Usage](#-how-to-use) · [Security](#-security)

</div>

---

## 📌 About the Project

AWS Automation Dashboard is a Python-based command-line application that provides a menu-driven interface for managing AWS resources.

Instead of typing every AWS CLI command manually, users can select an operation from the dashboard. Python collects the required input, executes the corresponding AWS CLI command through `subprocess.run()`, and displays the command output or error.

> **Built with:** Python + AWS CLI. This project uses the AWS CLI through Python's `subprocess` module; it does not use Boto3.

## ✨ Features

<table>
  <tr>
    <td width="50%">
      <h3>🖥️ EC2 Management</h3>
      <ul>
        <li>List EC2 instances</li>
        <li>Start, stop and reboot instances</li>
        <li>Launch new instances</li>
        <li>Terminate instances</li>
      </ul>
    </td>
    <td width="50%">
      <h3>🪣 S3 Management</h3>
      <ul>
        <li>List buckets</li>
        <li>Create and delete buckets</li>
        <li>List objects in a bucket</li>
        <li>Upload and delete objects</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>🔐 IAM Management</h3>
      <ul>
        <li>List and create IAM users</li>
        <li>Delete IAM users</li>
        <li>List and create IAM roles</li>
        <li>Attach and detach policies</li>
      </ul>
    </td>
    <td width="50%">
      <h3>⚡ Lambda Management</h3>
      <ul>
        <li>List Lambda functions</li>
        <li>Retrieve function details</li>
        <li>Create Lambda functions</li>
        <li>Delete Lambda functions</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <h3>🌐 API Gateway</h3>
      <p>API Gateway module is part of the project structure. Available operations depend on the implementation in the current version.</p>
    </td>
  </tr>
</table>

## 🧭 How It Works

<div align="center">

```text
              USER
               │
               ▼
       Python CLI Dashboard
               │
       Collects user input
               │
               ▼
       Python subprocess.run()
               │
               ▼
            AWS CLI
               │
       Uses local AWS credentials
               │
               ▼
          AWS Services
      ┌────────┼─────────┐
      ▼        ▼         ▼
     EC2       S3       IAM
               │
          Lambda / API Gateway
```

</div>

### Technology Stack

| Technology | Purpose |
|---|---|
| Python | Menu flow, user input and application logic |
| `subprocess` | Executes AWS CLI commands from Python |
| AWS CLI | Sends requests to AWS services |
| IAM | Controls access and permissions |
| ANSI escape codes | Adds colour to terminal output |

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
└── .gitignore
```

The structure above is a guide based on the project's modules. Your actual folders and files may differ as the project develops.

## 🚀 Getting Started

### 1. Prerequisites

Before running the dashboard, install:

- **Python 3** — to run the application.
- **AWS CLI** — to communicate with AWS.
- **An AWS account** — to access AWS services.
- **IAM permissions** — permissions for the operations you intend to perform.

Check that Python and AWS CLI are installed:

```bash
python --version
aws --version
```

### 2. Clone the Repository

Replace the placeholder with your GitHub repository URL.

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 3. Configure AWS CLI

Configure your own AWS credentials:

```bash
aws configure
```

The CLI will ask for:

```text
AWS Access Key ID
AWS Secret Access Key
Default region name
Default output format
```

Verify that authentication works:

```bash
aws sts get-caller-identity
```

If this command returns your AWS account and identity information, the CLI can authenticate successfully.

### 4. Run the Dashboard

```bash
python main.py
```

## 🕹️ How to Use

1. Start the application with `python main.py`.
2. Select an AWS service from the main menu.
3. Choose the operation you want to perform.
4. Enter the requested resource details, such as an instance ID, bucket name or function name.
5. Review the CLI output and any error messages.

<details>
  <summary><strong>Example: EC2 Operations</strong></summary>

  From the EC2 menu, you can choose to:

  - List instances
  - Start an instance
  - Stop an instance
  - Reboot an instance
  - Launch an instance
  - Terminate an instance

  For start, stop, reboot and termination operations, provide the target EC2 instance ID when prompted.
</details>

<details>
  <summary><strong>Example: S3 Operations</strong></summary>

  From the S3 menu, you can choose to:

  - List buckets
  - Create or delete a bucket
  - List objects in a bucket
  - Upload a local file
  - Delete an object

  For uploads, provide the local file path and destination bucket/object key.
</details>

<details>
  <summary><strong>Example: IAM and Lambda Operations</strong></summary>

  IAM operations work with users, roles and policies. Lambda operations work with function listing, details, creation and deletion.

  Some operations require additional AWS configuration. For example, creating a Lambda function requires a deployment ZIP file, a supported runtime, a handler and an IAM execution role ARN.
</details>

## 🔒 Security Notes

**Your AWS credentials should never be stored in this repository.**

- Do not hardcode access keys or secret keys in Python files.
- Do not commit your `.aws` credentials folder, `.env` files or private key files.
- Configure credentials locally using `aws configure`, or use an appropriate AWS role-based identity.
- Follow the principle of least privilege: grant only the permissions required for the operations you use.
- Be careful with destructive operations such as deleting S3 buckets, deleting IAM users and terminating EC2 instances.

The dashboard uses the credentials and permissions configured in the local AWS CLI environment. Anyone cloning the repository must configure their own AWS access.

## 🧰 Troubleshooting

<details>
  <summary><strong>Unable to locate credentials</strong></summary>

  Configure your own AWS credentials:

  ```bash
  aws configure
  ```

  Then verify:

  ```bash
  aws sts get-caller-identity
  ```
</details>

<details>
  <summary><strong>AccessDenied or AccessDeniedException</strong></summary>

  The AWS identity you're using does not have permission for the requested operation. Review the IAM policies attached to that identity and the resource policies involved.
</details>

<details>
  <summary><strong>ResourceNotFound or NoSuchEntity</strong></summary>

  Check that the resource exists, that its name or ID is correct, and that your AWS CLI is using the intended account and region. IAM is a global service, while many other AWS resources are region-specific.
</details>

<details>
  <summary><strong>AWS CLI is not recognized</strong></summary>

  Install AWS CLI and ensure it is available in your terminal's PATH. Open a new terminal and run:

  ```bash
  aws --version
  ```
</details>

## 🛣️ Project Roadmap

The following are potential improvements, not claims that they are already implemented.

- [ ] Add stronger input validation and clearer error handling
- [ ] Improve logging for AWS operations
- [ ] Add confirmation steps for destructive actions
- [ ] Complete and test API Gateway operations
- [ ] Add Lambda invocation support
- [ ] Add more resource details and cleaner output formatting
- [ ] Explore a browser-based interface

## 🎯 Learning Outcomes

This project is intended to practise:

- Python functions, modules and application structure
- Running external commands using `subprocess`
- AWS CLI command structure and output queries
- AWS resource management across multiple services
- IAM users, roles, trust relationships and policies
- Handling command success, failure and terminal output

## 🤝 Contributing

Suggestions and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the relevant AWS CLI operation in your own AWS account.
5. Submit a pull request with a clear description.

## ⚠️ Disclaimer

This is a learning and automation project. AWS operations can create billable resources or permanently delete resources. Review commands and costs before executing them. Test with non-production resources and use least-privilege IAM permissions.

---

<div align="center">

### ☁️ Built to learn. Automated with Python. Powered by AWS.

**If you find this project useful, consider giving the repository a ⭐**

</div>
