import json
import os

ContactBook = "cb.json"

def LoadContacts():
    if not os.path.exists(ContactBook) : return []
    try:
        with open(ContactBook, "r") as cb : return json.load(cb)
    except: 
        return []

def SaveContacts(contacts):
    with open(ContactBook, "w") as cb: json.dump(contacts,cb,indent=4)

def AddContact():
    contacts = LoadContacts()
    contacts.append({"name": input("Name:"), "phone": input("Phone:"), "email": input("Email:")})
    SaveContacts(contacts)
    print("Contact added into CB\n")

def ListContact():
    for c in LoadContacts():
        print(f"{c['name']} - {c['phone']} & {c['email']}")
    print()

def SearchContact():
    name = input("Name:").lower()
    for c in LoadContacts(): 
        if name in c['name'].lower():
            print(f"{c['name']} - {c['phone']} & {c['email']}")
    print()

def DeleteContact():
    name = input("Name:").lower()
    contacts =[c for c in LoadContacts() if name != c['name']]
    SaveContacts(contacts)
    print("Contact deleted\n")

while True:
    print("Welcome to contact book \n 1.Add contact | 2.List contact | 3.Search contact | 4.Delete contact | 5.Exit")
    choice = input("select a option[1 - 5] : ").strip()
    if not choice.isdigit():
        print("Invalid input: please enter a number between 1 and 5.\n")
        continue

    opt = int(choice)
    match opt:
        case 1:
            AddContact()
        case 2:
            ListContact()
        case 3:
            SearchContact()
        case 4:
            DeleteContact()
        case 5:
            break
        case _:
            print("Wrong input: please choose a valid option.\n")
        