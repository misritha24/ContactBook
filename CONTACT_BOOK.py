class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)

    def view_contact_list(self):
        print("Contact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact["name"].lower() or keyword.lower() in contact["phone"].lower()]
        return results

    def update_contact(self, contact_id, updated_contact):
        if 0 < contact_id <= len(self.contacts):
            self.contacts[contact_id - 1] = updated_contact
            print("Contact updated successfully.")
        else:
            print("Invalid contact ID.")

    def delete_contact(self, contact_id):
        if 0 < contact_id <= len(self.contacts):
            del self.contacts[contact_id - 1]
            print("Contact deleted successfully.")
        else:
            print("Invalid contact ID.")

    def display_menu(self):
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter contact name: ")
                phone = input("Enter contact phone: ")
                email = input("Enter contact email: ")
                address = input("Enter contact address: ")
                self.add_contact(name, phone, email, address)

            elif choice == 2:
                self.view_contact_list()

            elif choice == 3:
                keyword = input("Enter name or phone number to search: ")
                contacts = self.search_contact(keyword)
                if contacts:
                    print("\nSearch Results:")
                    for i, contact in enumerate(contacts, start=1):
                        print(f"{i}. {contact['name']} - {contact['phone']}")
                else:
                    print("No results found.")

            elif choice == 4:
                contact_id = int(input("Enter contact ID to update: "))
                if contact_id in [i + 1 for i, _ in enumerate(self.contacts)]:
                    updated_contact = {
                        "name": input("Enter updated name: "),
                        "phone": input("Enter updated phone: "),
                        "email": input("Enter updated email: "),
                        "address": input("Enter updated address: ")
                    }
                    self.update_contact(contact_id, updated_contact)

            elif choice == 5:
                contact_id = int(input("Enter contact ID to delete: "))
                self.delete_contact(contact_id)

            elif choice == 6:
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()
