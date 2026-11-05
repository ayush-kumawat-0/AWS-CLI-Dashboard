from core.aws_cli import run_aws_command
from services.ec2 import ec2_operations_list
from services.s3 import s3_operations_list
from services.iam import iam_operations_list
from services.lambda_service import lambda_operations_list
from services.apigateway import apigateway_operations_list

import subprocess
import os


# Terminal Colours
RESET = "\033[0m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GREY = "\033[90m"
BOLD = "\033[1m"


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
        print(f"\n{WHITE}{result.stdout}{RESET}")
        print(f"{GREEN}{BOLD}✓ Account information retrieved successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")


def main():

    os.system("cls" if os.name == "nt" else "clear")

    try:
        while True:

            print(f"\n{CYAN}{BOLD}======================================")
            print("       AWS AUTOMATION DASHBOARD")
            print(f"======================================{RESET}")

            print(f"{WHITE}1. EC2")
            print("2. S3")
            print("3. IAM")
            print("4. Lambda")
            # print("5. API Gateway")
            print("5. Account Information")
            print("6. Exit")
            print(f"{CYAN}======================================{RESET}")

            choice = input(f"\n{BLUE}Enter your choice: {RESET}").strip()

            if choice == "1":
                print(f"\n{YELLOW}EC2 module coming next...{RESET}")
                ec2_operations_list()

            elif choice == "2":
                print(f"\n{YELLOW}S3 module coming next...{RESET}")
                s3_operations_list()

            elif choice == "3":
                print(f"\n{YELLOW}IAM module coming next...{RESET}")
                iam_operations_list()

            elif choice == "4":
                print(f"\n{YELLOW}Lambda module coming next...{RESET}")
                lambda_operations_list()

            # elif choice == "5":
            #     print(f"\n{YELLOW}API Gateway module coming next...{RESET}")
            #     apigateway_operations_list()

            elif choice == "5":
                account_information()

            elif choice == "6":
                print(f"\n{RED}Exiting AWS Automation Dashboard...{RESET}")
                break

            else:
                print(f"\n{RED}Invalid choice. Enter 1-7.{RESET}")

    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Dashboard interrupted by user.{RESET}")
        print(f"{RED}Exiting AWS Automation Dashboard...{RESET}")
        raise SystemExit(0)


if __name__ == "__main__":
    main()