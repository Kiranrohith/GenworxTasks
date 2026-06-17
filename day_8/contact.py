from tabulate import tabulate

class ContactBook:

    def __init__(self):
        self.contact_book = {}
        self.next_contact_id = 0

    def add_contact(self):
        try:
            self.name = input("Enter name: ").strip()
            if not self.name:
                print("Error: Name cannot be empty.\n")
                return
            
            self.number = input("Enter mobile number: ").strip()
            if not self.number:
                print("Error: Mobile number cannot be empty.\n")
                return
            
            self.email = input("Enter email id: ").strip()
            if not self.email:
                print("Error: Email cannot be empty.\n")
                return
            
            self.category = input("Enter relationship category: ").strip()
            if not self.category:
                print("Error: Category cannot be empty.\n")
                return
            
            self.next_contact_id += 1
            self.contact_book.update({self.next_contact_id: {"name": self.name, "number": self.number, "email": self.email, "category": self.category}})
            print("Contact added\n")
        except KeyboardInterrupt:
            print("\nContact addition cancelled.\n")
        except Exception as e:
            print(f"Error adding contact: {e}\n")

    def list_contacts(self):
        try:
            if not self.contact_book:
                print("No contacts\n")
                return
            table_data = []
            for inner_id, inner_dict in self.contact_book.items():
                row = {"ID": inner_id}
                row.update(inner_dict) 
                table_data.append(row)
            print(tabulate(table_data, headers="keys", tablefmt="fancy_grid", numalign="left", stralign="left"))
            print()
        except Exception as e:
            print(f"Error displaying contacts: {e}\n")

    def delete_contact(self):
        try:
            contact_id = int(input("Enter contact id: "))
            if contact_id in self.contact_book:
                del self.contact_book[contact_id]
                print("Contact deleted\n")
                return
            print("No matching contact\n")
        except ValueError:
            print("Error: Please enter a valid numeric contact ID.\n")
        except KeyboardInterrupt:
            print("\nDeletion cancelled.\n")
        except Exception as e:
            print(f"Error deleting contact: {e}\n")

    def contactbook_modify(self):   
        try:
            while True:
                try:
                    print("1. Add contact\n2. List contacts")
                    print("3. Delete contact\n4. Exit")
                    choice = input("Select an option: ").strip()
                    if not choice.isdigit():
                        print("Invalid input: please enter a number between 1 and 4.\n")
                        continue

                    opt = int(choice)
                    match opt:
                        case 1:
                            self.add_contact()
                        case 2:
                            self.list_contacts()
                        case 3:
                            self.delete_contact()
                        case 4:
                            print("Exiting contact book.\n")
                            break
                        case _:
                            print("Wrong input: please choose a valid option.\n")
                except ValueError:
                    print("Error: Please enter a valid number.\n")
                except KeyboardInterrupt:
                    print("\nMenu navigation cancelled.\n")
        except Exception as e:
            print(f"Error in contact book menu: {e}\n")

