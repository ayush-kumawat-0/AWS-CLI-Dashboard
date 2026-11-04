
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


# Display IAM management menu
def iam_operations_list():

    clear_screen()

    try:
        while True:

            print(f"\n{CYAN}{BOLD}======================================")
            print("             IAM MANAGEMENT")
            print(f"======================================{RESET}")

            print(f"{WHITE}[1] List Users")
            print("[2] Create User")
            print("[3] Delete User")
            print("[4] List Roles")
            print("[5] Create Role")
            print("[6] Attach Policy")
            print("[7] Detach Policy")
            print("[8] Back to Main Menu")

            print(f"{CYAN}======================================{RESET}")

            choice = input(
                f"\n{BLUE}Enter your choice: {RESET}"
            ).strip()

            if choice == "1":
                list_users()

            elif choice == "2":
                create_user()

            elif choice == "3":
                delete_user()

            elif choice == "4":
                list_roles()

            elif choice == "5":
                create_role()

            elif choice == "6":
                attach_policy()

            elif choice == "7":
                detach_policy()

            elif choice == "8":
                clear_screen()
                break

            else:
                print(f"\n{RED}Invalid choice. Enter 1-8.{RESET}")

    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}IAM menu interrupted by user.{RESET}")
        print(f"{GREEN}Returning to the main program...{RESET}")


def list_users():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("          LIST USERS")
    print(f"============================{RESET}\n")

    print(f"{YELLOW}Retrieving IAM users...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ IAM users retrieved successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def create_user():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("         CREATE USER")
    print(f"============================{RESET}\n")

    user_name = input(
        f"{BLUE}Enter a name for the new IAM user: {RESET}"
    ).strip()

    print(f"\n{YELLOW}Creating IAM user...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ IAM user created successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def delete_user():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("         DELETE USER")
    print(f"============================{RESET}\n")

    print(f"{YELLOW}Retrieving IAM users...{RESET}\n")

    # Add AWS CLI command here to display existing users

    user_name = input(
        f"\n{BLUE}Enter the name of the IAM user to delete: {RESET}"
    ).strip()

    print(f"\n{YELLOW}Deleting IAM user...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ IAM user deleted successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def list_roles():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("          LIST ROLES")
    print(f"============================{RESET}\n")

    print(f"{YELLOW}Retrieving IAM roles...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ IAM roles retrieved successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def create_role():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("          CREATE ROLE")
    print(f"============================{RESET}\n")

    role_name = input(
        f"{BLUE}Enter a name for the new IAM role: {RESET}"
    ).strip()

    print(
        f"\n{YELLOW}A trust policy document is required to create an IAM role.{RESET}"
    )

    trust_policy_path = input(
        f"{BLUE}Enter the path to the trust policy JSON file: {RESET}"
    ).strip()

    print(f"\n{YELLOW}Creating IAM role...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ IAM role created successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def attach_policy():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("         ATTACH POLICY")
    print(f"============================{RESET}\n")

    user_name = input(
        f"{BLUE}Enter the IAM user name: {RESET}"
    ).strip()

    policy_arn = input(
        f"{BLUE}Enter the policy ARN to attach: {RESET}"
    ).strip()

    print(f"\n{YELLOW}Attaching policy to IAM user...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Policy attached successfully to IAM user.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def detach_policy():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("         DETACH POLICY")
    print(f"============================{RESET}\n")

    user_name = input(
        f"{BLUE}Enter the IAM user name: {RESET}"
    ).strip()

    policy_arn = input(
        f"{BLUE}Enter the policy ARN to detach: {RESET}"
    ).strip()

    print(f"\n{YELLOW}Detaching policy from IAM user...{RESET}\n")

    result = subprocess.run(
        [],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Policy detached successfully from IAM user.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()
