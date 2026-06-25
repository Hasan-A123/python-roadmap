# ====================================
# Project 6 - Contact Book
# Python Roadmap
# Store and manage contacts
# ====================================

def main():

    contacts = {}

    while True:
        print("\n==== CONTACT BOOK ====")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            print("Add Contact")
        
        elif choice == "2":
            print("View Contact")
        
        elif choice == "3":
            print("Search Contact")
        
        elif choice == "4":
            print("Delete Contact")
        
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid Operation")

if __name__ == "__main__":
    main()