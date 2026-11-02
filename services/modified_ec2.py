
# This is the EC2 code

from core.aws_cli import run_aws_command


def ec2_operations_list():
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

        choice = int(input("Enter your choice: ").strip())

        if choice == 1:
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

    print("\n============================")
    print("       LIST INSTANCES")
    print("============================")
    print("Showing instances...")

    result = run_aws_command(
        ["aws", "ec2", "describe-instances"]
    )

    if result["success"]:
        print(result["output"])
    else:
        print("AWS CLI Error:")
        print(result["error"])


def start_instance():

    print("\n============================")
    print("       START EC2 INSTANCE")
    print("============================")

    instance_id = input("Enter Instance ID: ").strip()

    print("Starting instance...")

    result = run_aws_command(
        ["aws", "ec2", "start-instances", "--instance-ids", instance_id]
    )

    if result["success"]:
        print(result["output"])
        print("✓ Instance start request successful.")
    else:
        print("AWS CLI Error:")
        print(result["error"])

    print("============================")


def stop_instance():

    print("\n============================")
    print("        STOP EC2 INSTANCE")
    print("============================")

    instance_id = input("Enter Instance ID: ").strip()

    print("Stopping instance...")

    result = run_aws_command(
        ["aws", "ec2", "stop-instances", "--instance-ids", instance_id]
    )

    if result["success"]:
        print(result["output"])
        print("✓ Instance stop request successful.")
    else:
        print("AWS CLI Error:")
        print(result["error"])

    print("============================")


def reboot_instance():

    print("\n============================")
    print("       REBOOT EC2 INSTANCE")
    print("============================")

    instance_id = input("Enter Instance ID: ").strip()

    print("Rebooting instance...")

    result = run_aws_command(
        ["aws", "ec2", "reboot-instances", "--instance-ids", instance_id]
    )

    if result["success"]:
        print(result["output"])
        print("✓ Instance reboot request successful.")
    else:
        print("AWS CLI Error:")
        print(result["error"])

    print("============================")


def launch_instance():

    print("\n============================")
    print("       LAUNCH EC2 INSTANCE")
    print("============================")

    ami_id = input("AMI ID: ").strip()
    instance_type = input("Instance type: ").strip()
    key_pair = input("Key pair: ").strip()
    security_grp = input("Security group ID: ").strip()
    subnet_id = input("Subnet ID: ").strip()

    print("Launching instance...")

    result = run_aws_command(
        [
            "aws", "ec2", "run-instances",
            "--image-id", ami_id,
            "--instance-type", instance_type,
            "--key-name", key_pair,
            "--security-group-ids", security_grp,
            "--subnet-id", subnet_id
        ]
    )

    if result["success"]:
        print(result["output"])
        print("✓ Instance launch request successful.")
    else:
        print("AWS CLI Error:")
        print(result["error"])

    print("============================")


def terminate_instance():

    print("\n============================")
    print("      TERMINATE EC2 INSTANCE")
    print("============================")

    instance_id = input("Enter Instance ID: ").strip()

    print("Terminating instance...")

    result = run_aws_command(
        ["aws", "ec2", "terminate-instances", "--instance-ids", instance_id]
    )

    if result["success"]:
        print(result["output"])
        print("✓ Instance termination request successful.")
    else:
        print("AWS CLI Error:")
        print(result["error"])

    print("============================")
