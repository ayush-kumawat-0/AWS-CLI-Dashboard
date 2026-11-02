#This is the lambda code

def lambda_operations_list():
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
