#This is the iam code

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


def iam_operations_list():


    try:

        while True:
            print("\n======================================")
            print("            IAM MANAGEMENT             ")
            print("=======================================")
            print("[1] List Users")
            print("[2] Create User")
            print("[3] Delete User")
            print("[4] List Roles")
            print("[5] Create Role")
            print("[6] Attach Policy")
            print("[7] Detach Policy")
            print("[8] Back to Main Menu")
            print("=======================================")

            choice = int(input("Enter your choice: ").strip())

            if choice == 1:
                print("List Users")
            elif choice == 2:
                print("Create User")
            elif choice == 3:
                print("Delete User")
            elif choice == 4:
                print("List Role")
            elif choice == 5:
                print("Create Role")
            elif choice == 6:
                print("Attach Policy")
            elif choice == 7:
                print("Detach Policy")
            elif choice == 8:
                print("Exit")
                break
            else:
                print("Invalid choice. Enter 1-8.")

    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Dashboard interrupted by user.{RESET}")
        print(f"{RED}Exiting AWS Automation Dashboard...{RESET}")
