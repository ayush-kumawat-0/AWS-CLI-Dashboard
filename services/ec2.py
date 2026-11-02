# This is the EC2 code
import subprocess
import os
import msvcrt


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause_and_clear():
    print("\nPress any key to continue...")
    msvcrt.getch()
    clear_screen()


def ec2_operations_list():
    clear_screen()

    while True:
        print("\n======================================")
        print("            EC2 MANAGEMENT")
        print("======================================")
        print("[1] List Instances")
        print("[2] Start Instance")
        print("[3] Stop Instance")
        print("[4] Reboot Instance")
        print("[5] Launch Instance")
        print("[6] Terminate Instance")
        print("[7] Back to Main Menu")
        print("======================================")

        choice = input("\nEnter your choice: ").strip()

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
            print("\nInvalid choice. Enter 1-7.")


def list_instance():

    clear_screen()

    print("\n============================")
    print("       LIST INSTANCES")
    print("============================")
    print("\nShowing instances...\n")

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
        print(result.stdout)
    else:
        print(result.stderr)

    pause_and_clear()


def start_instance():

    clear_screen()

    print("\n============================")
    print("      START INSTANCE")
    print("============================")
    print("\nStarting EC2 instance...\n")

    instance_id = input("Enter Instance ID: ").strip()

    result = subprocess.run(
        ["aws", "ec2", "start-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("\n✓ Instance start request successful.")
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()


def stop_instance():

    clear_screen()

    print("\n============================")
    print("       STOP INSTANCE")
    print("============================")
    print("\nStopping EC2 instance...\n")

    instance_id = input("Enter Instance ID: ").strip()

    result = subprocess.run(
        ["aws", "ec2", "stop-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("\n✓ Instance stop request successful.")
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()


def reboot_instance():

    clear_screen()

    print("\n============================")
    print("      REBOOT INSTANCE")
    print("============================")
    print("\nRebooting EC2 instance...\n")

    instance_id = input("Enter Instance ID: ").strip()

    result = subprocess.run(
        ["aws", "ec2", "reboot-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("\n✓ Instance reboot request successful.")
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()


def launch_instance():

    clear_screen()

    print("\n============================")
    print("       LAUNCH INSTANCE")
    print("============================")
    print("\nLaunching EC2 instance...\n")

    ami_id = input("AMI ID: ").strip()
    instance_type = input("Instance type: ").strip()

    print("\nLaunching instance...\n")

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
        print(result.stdout)
        print("\n✓ Instance launch request successful.")
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()


def terminate_instance():

    clear_screen()

    print("\n============================")
    print("      TERMINATE INSTANCE")
    print("============================")
    print("\nTerminating EC2 instance...\n")

    instance_id = input("Enter Instance ID: ").strip()

    result = subprocess.run(
        ["aws", "ec2", "terminate-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("\n✓ Instance termination request successful.")
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()