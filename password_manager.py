passwords = {}

while True:
    print("\n🔐 Password Manager")
    print("1. Add Password")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Delete Account")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        account = input("Enter account name: ")
        password = input("Enter password: ")

        passwords[account] = password
        print("✅ Password saved successfully!")

    elif choice == "2":
        if not passwords:
            print("No accounts found.")
        else:
            print("\n📋 Saved Accounts")
            for account, password in passwords.items():
                print(f"{account}: {password}")

    elif choice == "3":
        account = input("Enter account name to search: ")

        if account in passwords:
            print(f"🔑 Password: {passwords[account]}")
        else:
            print("❌ Account not found.")

    elif choice == "4":
        account = input("Enter account name to delete: ")

        if account in passwords:
            del passwords[account]
            print("🗑️ Account deleted successfully!")
        else:
            print("❌ Account not found.")

    elif choice == "5":
        print("Thank you for using Password Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
