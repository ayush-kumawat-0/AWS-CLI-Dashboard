#This is the apigateway code

def apigateway_operations_list():
    while True:
        print("\n======================================")
        print("            API GATEWAY FUNCTIONS             ")
        print("=======================================")
        print("[1] List APIs")
        print("[2] Get API")
        print("[3] Create API")
        print("[4] Delete API")
        print("[5] Back to Main Menu")
        print("=======================================")

        choice = int(input("Enter your choice: ").strip())

        if choice == 1:
            print("List APIs")
        elif choice == 2:
            print("Get API")
        elif choice == 3:
            print("Create API")
        elif choice == 4:
            print("Delete API")
        elif choice == 5:
            print("Exit")
            break
        else:
            print("Invalid choice. Enter 1-5.")
