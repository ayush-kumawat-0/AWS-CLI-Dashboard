# This is the S3 code
import subprocess
import os
import msvcrt


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause_and_clear():
    print("\nPress any key to continue...")
    msvcrt.getch()
    clear_screen()


def s3_operations_list():
    clear_screen()

    while True:
        print("\n======================================")
        print("             S3 MANAGEMENT")
        print("======================================")
        print("[1] List Buckets")
        print("[2] Create Bucket")
        print("[3] Delete Bucket")
        print("[4] List Objects")
        print("[5] Upload Object")
        print("[6] Download Object")
        print("[7] Delete Object")
        print("[8] Back to Main Menu")
        print("======================================")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            list_buckets()
        elif choice == "2":
            create_bucket()
        elif choice == "3":
            delete_bucket()
        elif choice == "4":
            list_object()
        elif choice == "5":
            upload_object()
        elif choice == "6":
            download_object()
        elif choice == "7":
            delete_object()
        elif choice == "8":
            clear_screen()
            break
        else:
            print("\nInvalid choice. Enter 1-8.")


def list_buckets():

    clear_screen()

    print("\n============================")
    print("       LIST BUCKETS")
    print("============================")
    print("\nShowing buckets...\n")

    result = subprocess.run(
        ["aws", "s3", "ls"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()


def create_bucket():

    clear_screen()

    print("\n============================")
    print("       CREATE BUCKET")
    print("============================\n")

    bucket_name = input("Enter Bucket Name: ").strip()
    print("\nCreating S3 bucket...\n")

    result = subprocess.run(
        ["aws", "s3", "mb", f"s3://{bucket_name}"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("\n✓ Bucket creation successful.")
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()


def delete_bucket():

    clear_screen()

    print("\n============================")
    print("       DELETE BUCKET")
    print("============================\n")

    bucket_name = input("Enter Bucket Name: ").strip()
    print("\nDeleting S3 bucket...\n")

    result = subprocess.run(
        ["aws", "s3", "rb", f"s3://{bucket_name}"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("\n✓ Bucket deletion successful.")
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()


def list_object():

    clear_screen()

    print("\n============================")
    print("       LIST OBJECTS")
    print("============================\n")

    bucket_name = input("Enter Bucket Name: ").strip()
    print("\nListing objects...\n")

    result = subprocess.run(
        ["aws", "s3", "ls", f"s3://{bucket_name}"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()


def upload_object():

    clear_screen()

    print("\n============================")
    print("       UPLOAD OBJECT")
    print("============================\n")

    bucket_name = input("Enter Bucket Name: ").strip()
    file_path = input("Enter File Path: ").strip()

    print("\nUploading object...\n")

    result = subprocess.run(
        ["aws", "s3", "cp", file_path, f"s3://{bucket_name}/"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("\n✓ Object upload successful.")
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()


def download_object():

    clear_screen()

    print("\n============================")
    print("      DOWNLOAD OBJECT")
    print("============================\n")

    bucket_name = input("Enter Bucket Name: ").strip()
    object_key = input("Enter Object Key: ").strip()
    destination_path = input("Enter Destination Path: ").strip()

    print("\nDownloading object...\n")

    result = subprocess.run(
        [
            "aws", "s3", "cp",
            f"s3://{bucket_name}/{object_key}",
            destination_path
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("\n✓ Object download successful.")
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()


def delete_object():

    clear_screen()

    print("\n============================")
    print("       DELETE OBJECT")
    print("============================\n")

    bucket_name = input("Enter Bucket Name: ").strip()
    object_key = input("Enter Object Key: ").strip()

    print("\nDeleting object...\n")

    result = subprocess.run(
        ["aws", "s3", "rm", f"s3://{bucket_name}/{object_key}"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("\n✓ Object deletion successful.")
    else:
        print("\nAWS CLI Error:")
        print(result.stderr)

    pause_and_clear()