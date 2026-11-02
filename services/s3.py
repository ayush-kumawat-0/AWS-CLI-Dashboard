#This is the s3 code
import subprocess

def s3_operations_list():
    while True:
        print("\n======================================")
        print("            S3 MANAGEMENT             ")
        print("=======================================")
        print("[1] List Buckets")
        print("[2] Create Bucket")
        print("[3] Delete Bucket")
        print("[4] List Objects")
        print("[5] Upload Object")
        print("[6] Download Object")
        print("[7] Delete Object")
        print("[8] Back to Main Menu")
        print("=======================================")

        choice = int(input("Enter your choice: ").strip())

        if choice == 1:
            print("List Buckets")
            list_buckerts()
        elif choice == 2:
            print("Create Bucket")
            create_bucket()
        elif choice == 3:
            print("Delete Bucket")
            delete_bucket()
        elif choice == 4:
            print("List Object")
            list_object()
        elif choice == 5:
            print("Upload Objec")
            upload_object()
        elif choice == 6:
            print("Download Object")
            download_object()
        elif choice == 7:
            print("Delete Object")
            delete_object()
        elif choice == 8:
            print("Exit")
            break
        else:
            print("Invalid choice. Enter 1-8.")


def list_buckerts():
    print("\n============================")
    print("     LIST BUCKETS      ")
    print("============================")
    print("Showing Buckets...")

    result = subprocess.run (
        ["aws", "s3", "ls"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("✓ Bucket listing successfully.")
    else:
        print(result.stderr)

    print("============================")

def create_bucket():
    print("\n============================")
    print("     CREATE BUCKET      ")
    print("============================")
    bucket_name = input("Enter Bucket Name: ")
    print("Creating bucket...")

    result = subprocess.run (
        ["aws", "s3", "mb", f"s3://{bucket_name}"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("✓ Bucket creation successful.")
    else:
        print(result.stderr)

    print("\n============================")

def delete_bucket():
    print("\n============================")
    print("     DELETE BUCKET      ")
    print("============================")
    bucket_name = input("Enter Bucket Name: ")
    print("Deleting bucket...")

    result = subprocess.run (
        ["aws", "s3", "rb", f"s3://{bucket_name}"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("✓ Bucket deletion successful.")
    else:
        print(result.stderr)

    print("============================")


def list_object():
    print("\n============================")
    print("     LIST OBJECTS      ")
    print("============================")
    bucket_name = input("Enter Bucket Name: ")
    print("Listing objects...")

    result = subprocess.run (
        ["aws", "s3", "ls", f"s3://{bucket_name}"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("✓ Object listing successful.")
    else:
        print(result.stderr)

    print("============================")



def upload_object():
    print("\n============================")
    print("     UPLOAD OBJECT      ")
    print("============================")
    bucket_name = input("Enter Bucket Name: ")
    file_path = input("Enter File Path: ")
    print("Uploading object...")

    result = subprocess.run (
        ["aws", "s3", "cp", file_path, f"s3://{bucket_name}/"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("✓ Object upload successful.")
    else:
        print(result.stderr)

    print("============================")


def download_object():
    print("\n============================")
    print("     DOWNLOAD OBJECT      ")
    print("============================")
    bucket_name = input("Enter Bucket Name: ")
    object_key = input("Enter Object Key: ")
    destination_path = input("Enter Destination Path: ")
    print("Downloading object...")

    result = subprocess.run (
        ["aws", "s3", "cp", f"s3://{bucket_name}/{object_key}", destination_path],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("✓ Object download successful.")
    else:
        print(result.stderr)

    print("============================")


def delete_object():
    print("\n============================")
    print("     DELETE OBJECT      ")
    print("============================")
    bucket_name = input("Enter Bucket Name: ")
    object_key = input("Enter Object Key: ")
    print("Deleting object...")

    result = subprocess.run (
        ["aws", "s3", "rm", f"s3://{bucket_name}/{object_key}"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(result.stdout)
        print("✓ Object deletion successful.")
    else:
        print(result.stderr)

    print("============================")



