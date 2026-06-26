# ====================================
# Project 6 - Contact Book
# Python Roadmap
# Store and manage contacts using a dictionary
# Supports: Add, View, Search, Delete, Update
# ====================================


def main():

    # Dictionary to store contacts in format:
    # { "name": "phone_number" }
    contacts = {}

    while True:
        # Main menu display
        print("\n==== CONTACT BOOK ====")
        print(f"Contacts: {len(contacts)}")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        # =========================
        # Add Contact
        # =========================
        if choice == "1":
            print("Add Contact")

            name = input("What is the name?: ").strip()
            phone_number = input("What is the phone number?: ").strip()

            # Validate input
            if name in contacts:
                print("Contact already exists")
                continue
            if not name or not phone_number:
                print("Empty contact not allowed")
                continue

            # Store contact
            contacts[name] = phone_number
            print(f'"{name}" added successfully!')

        # =========================
        # View All Contacts
        # =========================
        elif choice == "2":
            print("\nYour Contacts")

            if not contacts:
                print("No contacts found")
            else:
                # Loop through dictionary items (name + phone)
                for i, (name, phone_number) in enumerate(contacts.items(), start=1):
                    print(f"{i}. {name}: {phone_number}")

        # =========================
        # Search Contact
        # =========================
        elif choice == "3":
            print("Search Contact")

            name = input("Enter contact name: ").strip()

            # Check if contact exists
            if name in contacts:
                print(f"Name: {name}")
                print(f"Phone Number: {contacts[name]}")
            else:
                print("Contact not found")

        # =========================
        # Delete Contact
        # =========================
        elif choice == "4":
            print("Delete Contact")

            name = input("Enter contact name: ").strip()

            if name in contacts:
                # Confirmation before deletion
                delete_contact = input("Are you sure? (yes/no): ").lower()

                if delete_contact == "yes":
                    del contacts[name]
                    print(f'"{name}" deleted successfully!')
                else:
                    print("Deletion Cancelled")
            else:
                print("Contact not found")

        # =========================
        # Update Contact
        # =========================
        elif choice == "5":
            print("Update Contact")

            name = input("Enter contact name: ").strip()

            if name in contacts:
                # Show current number
                print(f"Current Number: {contacts[name]}")

                # Get new number
                new_number = input("Enter new number: ").strip()

                # Validate update
                if not new_number:
                    print("Phone number cannot be empty")
                    continue

                # Update dictionary
                contacts[name] = new_number
                print(f'"{name}" updated successfully!')
            else:
                print("Contact not found")

        # =========================
        # Exit program
        # =========================
        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid Operation")


if __name__ == "__main__":
    main()