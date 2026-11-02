#This is the ec2 code
import subprocess
import os
import msvcrt

def ec2_operations_list():
    while True:
        print("\n======================================")
        print("            EC2 MANAGEMENT             ")
        print("======================================")
        print("[1] List Instances")
        print("[2] Start Instance")
        print("[3] Stop Instance")
        print("[4] Reboot Instance")
        print("[5] Launch Instance")
        print("[6] Terminate Instance")
        print("[7] Back to Main Menu")
        print("=======================================")

        choice = int(input("Enter your choice: ").strip())

        if choice == 1:
            print("EC2 Instance List")
            list_instance()
        elif choice == 2:
            start_instance()
        elif choice == 3:
            stop_instance()
        elif choice == 4:
            reboot_instance()
        elif choice == 5:
            launch_instance()
        elif choice == 6:
            terminate_instance()
        elif choice == 7:
            print("Exit")
            break
        else:
            print("Invalid choice. Enter 1-7.")


def list_instance():

    # os.system("cls" if os.name == "nt" else "clear")


    print("\n============================")
    print("     LIST INSTANCE      ")
    print("============================")
    print("Showing instance...")

    result = subprocess.run (
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

    print("============================")
    print("\nPress any key to continue...")
    msvcrt.getch()
    # input("\nPress Enter to continue...")

def start_instance():

    print("\n============================")
    print("     START EC2 INSTANCE      ")
    print("============================")
    instance_id = input("Enter Instance ID: ")
    print("Starting instance...")

    result = subprocess.run (
        ["aws", "ec2", "start-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(result.stdout)
        print("✓ Instance start request successful.")

    else:
        print(result.stderr)

    print("============================")



    
def stop_instance():

    print("\n============================")
    print("     STOP EC2 INSTANCE      ")
    print("============================")
    instance_id = input("Enter Instance ID: ")
    print("Stopping instance...")

    result = subprocess.run (
        ["aws", "ec2", "stop-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(result.stdout)
        print("✓ Instance stoped request successful.")

    else:
        print(result.stderr)

    print("============================")



def reboot_instance():

    print("\n============================")
    print("     REBOOT EC2 INSTANCE      ")
    print("============================")
    instance_id = input("Enter Instance ID: ")
    print("Rebooting instance...")

    result = subprocess.run (
        ["aws", "ec2", "reboot-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(result.stdout)
        print("✓ Instance reboot request successful.")

    else:
        print(result.stderr)

    print("============================")



def launch_instance():

    print("\n============================")
    print("     LAUNCH EC2 INSTANCE      ")
    print("============================")
    ami_id = input("AMI ID: ")
    instance_type = input("Instance type: ")
    # key_pair = input("Key pair: ")
    # security_grp = input("Security group: ")
    # subnet_id = input("Subnet ID: ")
    print("Launching instance...")

    result = subprocess.run (
        ["aws", "ec2", "run-instances", "--image-id", ami_id, "--instance-type", instance_type],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(result.stdout)
        print("✓ Instance launched successful.")

    else:
        print(result.stderr)

    print("============================")



def terminate_instance():

    print("\n============================")
    print("     TERMINATE EC2 INSTANCE      ")
    print("============================")
    instance_id = input("Enter Instance ID: ")
    print("Terminating instance...")

    result = subprocess.run (
        ["aws", "ec2", "terminate-instances", "--instance-ids", instance_id],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(result.stdout)
        print("✓ Instance termination request successful.")

    else:
        print(result.stderr)

    print("============================")