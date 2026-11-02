#This is the iam code

def iam_operations_list():
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
