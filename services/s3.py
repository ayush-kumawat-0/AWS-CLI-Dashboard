import subprocess
import os
import msvcrt

# To clear the screen after any input
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


def s3_operations_list():
    clear_screen()

    try:
        while True:
            print(f"\n{CYAN}{BOLD}======================================")
            print("             S3 MANAGEMENT")
            print(f"======================================{RESET}")
            print(f"{WHITE}[1] List Buckets")
            print("[2] Create Bucket")
            print("[3] Delete Bucket")
            print("[4] List Objects")
            print("[5] Upload Object")
            # print("[6] Download Object")
            print(f"[6] Delete Object")
            print(f"[7] Back to Main Menu{RESET}")
            print(f"{CYAN}======================================{RESET}")

            choice = input(f"\n{BLUE}Enter your choice: {RESET}").strip()

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
            # elif choice == "6":
            #     download_object()
            elif choice == "6":
                delete_object()
            elif choice == "7":
                clear_screen()
                break
            else:
                print(f"\n{RED}Invalid choice. Enter 1-7.{RESET}")

    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Dashboard interrupted by user.{RESET}")
        print(f"{RED}Exiting AWS Automation Dashboard...{RESET}")


def show_all_buckets():
    print(f"{YELLOW}Fetching available buckets...{RESET}\n")

    result = subprocess.run(
        ["aws", "s3api", "list-buckets", "--query", "Buckets[].[Name,CreationDate]","--output", "table"] ,
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:{RESET}")
        print(f"{RED}{result.stderr}{RESET}")


def list_buckets():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("       LIST BUCKETS")
    print(f"============================{RESET}")
    print(f"\n{YELLOW}Showing buckets...{RESET}\n")

    result = subprocess.run(
        ["aws", "s3api", "list-buckets", "--query", "Buckets[].[Name,CreationDate]","--output", "table"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:{RESET}")
        print(f"{RED}{result.stderr}{RESET}")

    pause_and_clear()


def create_bucket():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("       CREATE BUCKET")
    print(f"============================{RESET}\n")

    show_all_buckets()

    bucket_name = input(f"\n{BLUE}Enter Bucket Name: {RESET}").strip()
    print(f"\n{YELLOW}Creating your S3 bucket...{RESET}\n")

    result = subprocess.run(
        ["aws", "s3", "mb", f"s3://{bucket_name}","--output", "table"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ Bucket creation successful.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


def delete_bucket():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("       DELETE BUCKET")
    print(f"============================{RESET}\n")

    show_all_buckets()

    bucket_name = input(f"\n{BLUE}Enter the name of the bucket to delete: {RESET}").strip()

    confirmation = input(f"{BLUE}Are you sure you want to continue? (y/n): {RESET}").strip().lower()

    if confirmation == "y":
        print(f"\n{YELLOW}Deleting your S3 bucket...{RESET}\n")

        result = subprocess.run(
            ["aws", "s3", "rb", f"s3://{bucket_name}","--output", "table"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"{WHITE}{result.stdout}{RESET}")
            print(f"\n{RED}{BOLD}✓ Bucket deletion successful.{RESET}")
        else:
            print(f"\n{RED}AWS CLI Error:")
            print(f"{result.stderr}{RESET}")

        pause_and_clear()

    else:
            print(f"\n{YELLOW}Bucket deletion cancelled.{RESET}")


def list_object():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("       LIST OBJECTS")
    print(f"============================{RESET}\n")

    show_all_buckets()

    bucket_name = input(f"{BLUE}Enter Bucket Name: {RESET}").strip()
    print(f"\n{YELLOW}Retrieving bucket contents...{RESET}\n")

    result = subprocess.run(
        # ["aws", "s3", "ls", f"s3://{bucket_name}"],
        ["aws","s3api","list-objects","--bucket", bucket_name, "--query", "Contents[].{Key:Key,Last_Modified:LastModified,Size:Size}","--output", "table"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()



def show_all_objects(bucket_name):

    print(f"{YELLOW}Fetching objects from S3...{RESET}\n")

    # bucket_name = input(f"{BLUE}Enter Bucket Name: {RESET}").strip()
    # print(f"\n{YELLOW}Listing objects...{RESET}\n")

    result = subprocess.run(
        # ["aws", "s3", "ls", f"s3://{bucket_name}"],
        ["aws","s3api","list-objects","--bucket", f"{bucket_name}", "--query", "Contents[].{Key:Key,Last_Modified:LastModified,Size:Size}","--output", "table"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")


def upload_object():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("       UPLOAD OBJECT")
    print(f"============================{RESET}\n")

    show_all_buckets()

    bucket_name = input(f"{BLUE}Enter the destination bucket name: {RESET}").strip()
    file_path = input(f"{BLUE}Enter the local file path to upload: {RESET}").strip()
    object_key = input(f"{BLUE}Enter the destination path in S3 (e.g., images/photo.png): {RESET}").strip()

    print(f"\n{YELLOW}Uploading file to S3...{RESET}\n")

    result = subprocess.run(
        # Old command
        # ["aws", "s3", "cp", file_path, f"s3://{bucket_name}/"],

        # New command
        # --key = It is the path in s3, how it's stored (images/img.png)
        # --body =  It is the local path in my system (C:/Ayush/Doc/img.png)
        ["aws" , "s3api" , "put-object", "--bucket",bucket_name,"--key",object_key,"--body",file_path ,"--output", "table"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"{WHITE}{result.stdout}{RESET}")
        print(f"\n{GREEN}{BOLD}✓ File uploaded successfully.{RESET}")
    else:
        print(f"\n{RED}AWS CLI Error:")
        print(f"{result.stderr}{RESET}")

    pause_and_clear()


# def download_object():

#     clear_screen()

#     print(f"\n{CYAN}{BOLD}============================")
#     print("      DOWNLOAD OBJECT")
#     print(f"============================{RESET}\n")

#     bucket_name = input(f"{BLUE}Enter Bucket Name: {RESET}").strip()
#     object_key = input(f"{BLUE}Enter Object Key: {RESET}").strip()
#     destination_path = input(f"{BLUE}Enter Destination Path: {RESET}").strip()

#     print(f"\n{YELLOW}Downloading object...{RESET}\n")

#     result = subprocess.run(
#         [
#             "aws", "s3", "cp",
#             f"s3://{bucket_name}/{object_key}",
#             destination_path
#         ],
#         capture_output=True,
#         text=True
#     )

#     if result.returncode == 0:
#         print(f"{WHITE}{result.stdout}{RESET}")
#         print(f"\n{GREEN}{BOLD}✓ Object download successful.{RESET}")
#     else:
#         print(f"\n{RED}AWS CLI Error:")
#         print(f"{result.stderr}{RESET}")

#     pause_and_clear()


def delete_object():

    clear_screen()

    print(f"\n{CYAN}{BOLD}============================")
    print("       DELETE OBJECT")
    print(f"============================{RESET}\n")

    show_all_buckets()

    bucket_name = input(f"{BLUE}Enter the bucket name containing the object: {RESET}").strip()

    show_all_objects(bucket_name)
    object_key = input(f"{BLUE}Enter the object key to delete (e.g., images/photo.png): {RESET}").strip()

    confirmation = input(f"{BLUE}Are you sure you want to continue? (y/n): {RESET}").strip().lower()

    if confirmation == "y":

        print(f"\n{YELLOW}Deleting object from S3...{RESET}\n")

        result = subprocess.run(
            # ["aws", "s3", "rm", f"s3://{bucket_name}/{object_key}"],
            ["aws", "s3api", "delete-object", "--bucket", bucket_name, "--key",object_key,"--output", "table"],

            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"{WHITE}{result.stdout}{RESET}")
            print(f"\n{RED}{BOLD}✓ Object deleted successfully.{RESET}")
        else:
            print(f"\n{RED}AWS CLI Error:")
            print(f"{result.stderr}{RESET}")

        pause_and_clear()

    else:
        print(f"\n{YELLOW}Object deletion cancelled.{RESET}")