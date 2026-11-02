from core.aws_cli import run_aws_command
from services.ec2 import ec2_operations_list
from services.s3 import s3_operations_list
from services.iam import iam_operations_list
from services.lambda_service import lambda_operations_list
from services.apigateway import apigateway_operations_list

import subprocess
import os


# def account_information():
#     result = run_aws_command(
#         ["aws", "sts", "get-caller-identity"]
#     )

#     if result["success"]:
#         print(result["output"])
#     else:
#         print("AWS CLI Error:")
#         print(result["error"])

def account_information():
    result = subprocess.run(
            ["aws", "sts", "get-caller-identity"],
            capture_output=True,
            text=True
        )
    
    if result.returncode == 0:
            print(result.stdout)
            print("✓ Account information retrieved successfully.")
    else:
            print(result.stderr)
    


def main():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("\n======================================")
        print("       AWS AUTOMATION DASHBOARD")
        print("======================================")
        print("1. EC2")
        print("2. S3")
        print("3. IAM")
        print("4. Lambda")
        print("5. API Gateway")
        print("6. Account Information")
        print("7. Exit")
        print("======================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("EC2 module coming next...")
            ec2_operations_list()
        elif choice == "2":
            print("S3 module coming next...")
            s3_operations_list()
        elif choice == "3":
            print("IAM module coming next...")
            iam_operations_list()
        elif choice == "4":
            print("Lambda module coming next...")
            lambda_operations_list()
        elif choice == "5":
            print("API Gateway module coming next...")
            apigateway_operations_list()
        elif choice == "6":
            account_information()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1-7.")


if __name__ == "__main__":
    main()