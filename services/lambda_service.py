#This is the lambda code

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


def lambda_operations_list():

    try:
        while True:
            print("\n======================================")
            print("            Lambda FUNCTIONS             ")
            print("=======================================")
            print("[1] List Functions")
            print("[2] Get Function")
            print("[3] Create Function")
            print("[4] Invoke Function")
            print("[5] Delete Function")
            print("[6] Back to Main Menu")
            print("=======================================")

            choice = int(input("Enter your choice: ").strip())

            if choice == 1:
                print("List Functions")
            elif choice == 2:
                print("Get Function")
            elif choice == 3:
                print("Create Function")
            elif choice == 4:
                print("Invoke Function")
            elif choice == 5:
                print("Delete Function")
            elif choice == 6:
                print("Exit")
                break
            else:
                print("Invalid choice. Enter 1-6.")

    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Dashboard interrupted by user.{RESET}")
        print(f"{RED}Exiting AWS Automation Dashboard...{RESET}")
