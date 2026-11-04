
import subprocess
import os
import msvcrt


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


# Clear terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Pause before returning to the menu
def pause_and_clear():
    print(f"\n{GREY}Press any key to continue...{RESET}")
    msvcrt.getch()
    clear_screen()


# Display Lambda management menu
def lambda_operations_list():

    clear_screen()

    try:
        while True:

            print(f"\n{CYAN}{BOLD}======================================")
            print("             LAMBDA FUNCTIONS")
            print(f"======================================{RESET}")

            print(f"{WHITE}[1] List Functions")
            print("[2] Get Function")
            print("[3] Create Function")
            print("[4] Invoke Function")
            print("[5] Delete Function")
            print("[6] Back to Main Menu")

            print(f"{CYAN}======================================{RESET}")

            choice = input(
                f"\n{BLUE}Enter your choice: {RESET}"
            ).strip()

            if choice == "1":
                list_functions()

            elif choice == "2":
                get_function()

            elif choice == "3":
                create_function()

            elif choice == "4":
                invoke_function()

            elif choice == "5":
                delete_function()

            elif choice == "6":
                clear_screen()
                break

            else:
                print(f"\n{RED}Invalid choice. Enter 1-6.{RESET}")

    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Lambda menu interrupted by user.{RESET}")
        print(f"{GREEN}Returning to the main program...{RESET}")


def list_functions():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("        LIST FUNCTIONS")
    print(f"============================{RESET}\n")

    print(f"{YELLOW}Retrieving Lambda functions...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Lambda functions retrieved successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def get_function():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("         GET FUNCTION")
    print(f"============================{RESET}\n")

    function_name = input(
        f"{BLUE}Enter the name of the Lambda function: {RESET}"
    ).strip()

    print(f"\n{YELLOW}Retrieving Lambda function details...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Lambda function details retrieved successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def create_function():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("        CREATE FUNCTION")
    print(f"============================{RESET}\n")

    function_name = input(
        f"{BLUE}Enter a name for the new Lambda function: {RESET}"
    ).strip()

    runtime = input(
        f"{BLUE}Enter the Lambda runtime (e.g., python3.12): {RESET}"
    ).strip()

    role_arn = input(
        f"{BLUE}Enter the IAM execution role ARN: {RESET}"
    ).strip()

    zip_path = input(
        f"{BLUE}Enter the path to the deployment ZIP file: {RESET}"
    ).strip()

    print(f"\n{YELLOW}Creating Lambda function...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Lambda function created successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def invoke_function():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("        INVOKE FUNCTION")
    print(f"============================{RESET}\n")

    function_name = input(
        f"{BLUE}Enter the name of the Lambda function to invoke: {RESET}"
    ).strip()

    payload = input(
        f"{BLUE}Enter the JSON payload (leave empty for no input): {RESET}"
    ).strip()

    print(f"\n{YELLOW}Invoking Lambda function...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Lambda function invoked successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def delete_function():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("        DELETE FUNCTION")
    print(f"============================{RESET}\n")

    print(f"{YELLOW}Retrieving Lambda functions...{RESET}\n")

    # Add AWS CLI command here to display existing functions

    function_name = input(
        f"\n{BLUE}Enter the name of the Lambda function to delete: {RESET}"
    ).strip()

    print(f"\n{YELLOW}Deleting Lambda function...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Lambda function deleted successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()
