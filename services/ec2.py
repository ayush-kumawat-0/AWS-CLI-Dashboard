# This is the EC2 code
import subprocess
import os
import msvcrt


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause_and_clear():
    print(f"\n{GREY}Press any key to continue...{RESET}")
    msvcrt.getch()
    clear_screen()


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


def ec2_operations_list():
    clear_screen()

    try:
        while True:
            print(f"\n{CYAN}{BOLD}======================================")
            print("            EC2 MANAGEMENT")
            print(f"======================================{RESET}")
            print(f"{WHITE}[1] List Instances")
            print("[2] Start Instance")
            print("[3] Stop Instance")
            print("[4] Reboot Instance")
            print("[5] Launch Instance")
            print("[6] Terminate Instance")
            print(f"[7] Back to Main Menu{RESET}")
            print(f"{CYAN}======================================{RESET}")

            choice = input(f"\n{BLUE}Enter your choice: {RESET}").strip()

            if choice == "1":
                list_instance()
            elif choice == "2":
                start_instance()
            elif choice == "3":
                stop_instance()
            elif choice == "4":
                reboot_instance()
            elif choice == "5":
                launch_instance()
            elif choice == "6":
                terminate_instance()
            elif choice == "7":
                clear_screen()
                break
            else:
                print(f"\n{RED}Invalid choice. Enter 1-7.{RESET}")

    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Dashboard interrupted by user.{RESET}")
        print(f"{RED}Exiting AWS Automation Dashboard...{RESET}")


def show_all_instances():

    print(f"{YELLOW}Waiting for instances...{RESET}\n")

    result = subprocess.run(
        [
            "aws", "ec2", "describe-instances",
            "--query",
            "Reservations[].Instances[].[InstanceId,State.Name,InstanceType,PrivateIpAddress]",
            "--output", "table"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
    else:
        print(f"{RED}{result.stderr}{RESET}")


def list_instance():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("       LIST INSTANCES")
    print(f"============================{RESET}")
    print(f"\n{YELLOW}Showing instances...{RESET}\n")

    result = subprocess.run(
        [
            "aws", "ec2", "describe-instances",
            "--query",
            "Reservations[].Instances[].[InstanceId,State.Name,InstanceType,PrivateIpAddress]",
            "--output", "table"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def start_instance():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("      START INSTANCE")
    print(f"============================{RESET}\n")

    show_all_instances()

    instance_id = input(f"\n{BLUE}Enter Instance ID: {RESET}").strip()
    print(f"\n{YELLOW}Starting EC2 instance...{RESET}\n")

    result = subprocess.run(
        ["aws", "ec2", "start-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Instance start request successful.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def stop_instance():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("       STOP INSTANCE")
    print(f"============================{RESET}\n")

    show_all_instances()

    instance_id = input(f"\n{BLUE}Enter Instance ID: {RESET}").strip()
    print(f"\n{YELLOW}Stopping EC2 instance...{RESET}\n")

    result = subprocess.run(
        ["aws", "ec2", "stop-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Instance stop request successful.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def reboot_instance():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("      REBOOT INSTANCE")
    print(f"============================{RESET}\n")

    show_all_instances()

    instance_id = input(f"\n{BLUE}Enter Instance ID: {RESET}").strip()
    print(f"\n{YELLOW}Rebooting EC2 instance...{RESET}\n")

    result = subprocess.run(
        ["aws", "ec2", "reboot-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Instance reboot request successful.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def launch_instance():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("       LAUNCH INSTANCE")
    print(f"============================{RESET}\n")

    ami_id = input(f"{BLUE}AMI ID: {RESET}").strip()
    instance_type = input(f"{BLUE}Instance type: {RESET}").strip()

    print(f"\n{YELLOW}Launching EC2 instance...{RESET}\n")

    result = subprocess.run(
        [
            "aws", "ec2", "run-instances",
            "--image-id", ami_id,
            "--instance-type", instance_type
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Instance launch request successful.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def terminate_instance():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("      TERMINATE INSTANCE")
    print(f"============================{RESET}\n")

    show_all_instances()

    instance_id = input(f"\n{BLUE}Enter Instance ID: {RESET}").strip()
    print(f"\n{YELLOW}Terminating EC2 instance...{RESET}\n")

    result = subprocess.run(
        ["aws", "ec2", "terminate-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Instance termination request successful.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()