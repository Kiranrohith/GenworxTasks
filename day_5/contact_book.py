from tabulate import tabulate
contact_book = {}
next_contact_id = 0
def add_contact():
    name = input("Enter name: ")
    number = input("Enter mobile number: ")
    email = input("Enter email id: ")
    category = input("Enter relationship category: ")
    global next_contact_id
    next_contact_id+=1
    contact_book.update({next_contact_id:{"name":name,"number":number,"email":email, "category":category}})
    print("Contact added")

def list_contacts():
    if not contact_book:
        print("No contacts")
        return
    table_data = []
    for inner_id, inner_dict in contact_book.items():
        row = {"ID": inner_id}
        row.update(inner_dict) 
        table_data.append(row)
    print(tabulate(table_data, headers="keys", tablefmt="fancy_grid", numalign="left", stralign="left"))

def delete_contact():
    contact_id = int(input("Enter contact id: "))
    if contact_id in contact_book:
        del contact_book[contact_id]
        print("contact deleted")
        return
    print("No matching contact")
    
while(True):
    print("1. Add contact\n2. List contacts\n3. Delete contact\n4. Exit")
    choice = input("Select an option: ").strip()
    if not choice.isdigit():
        print("Invalid input: please enter a number between 1 and 4.\n")
        continue

    opt = int(choice)
    match opt:
        case 1:
            add_contact()
        case 2:
            list_contacts()
        case 3:
            delete_contact()
        case 4:
            break
        case _:
            print("Wrong input: please choose a valid option.\n")
