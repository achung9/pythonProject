from contact.contact import Contact
from contact.contactManager import ContactManager

def main():
    my_contact = ContactManager()
    while True:
        # Sử dụng chuỗi nhiều dòng để menu trông đẹp hơn
        print("\n--- CONTACT MANAGER MENU ---")
        num = input("""Choose a function:
        1. Add contact
        2. Find contact
        3. Delete contact
        4. Change contact name
        5. Exit
        Your choice: """)

        match num:
            case "1": # Thêm dấu nháy kép để so sánh chuỗi
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                contact = Contact(name, email, phone_number)
                # Nên có hàm addContact trong ContactManager
                my_contact.contacts.append(contact)
            case "2":
                name = input("Enter name to find: ")
                my_contact.findContact(name)
            case "3":
                name = input("Enter name to delete: ")
                my_contact.deleteContact(name)
            case "4":
                name = input("Enter contact name to change: ")
                newName = input("Enter the NEW name: ")
                # Đảm bảo tên hàm này tồn tại trong ContactManager của bạn
                my_contact.changeContactName(name, newName)
            case "5":
                print("Exiting program...")
                break
            case _:
                print("❌ Invalid choice, please try again.")

    print("\n--- Final Contact List ---")
    my_contact.printContacts()

if __name__ == "__main__":
    main()