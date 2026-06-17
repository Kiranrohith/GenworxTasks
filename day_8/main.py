try:
    from contact import ContactBook, tabulate
    from todo import add_task, complete_task, list_tasks, todolist, task_modifier
except ImportError as e:
    print(f"Error: Failed to import required modules - {e}")
    exit(1)

try:
    try:
        choice = int(input("1.Contact Book\n2.Todolist\nEnter your choice:"))
    except ValueError:
        print("Give only number choice 1 or 2")
    if choice == 1:
        contact_book = ContactBook()
        contact_book.contactbook_modify()
    elif choice == 2:
        task_modifier()
    else:
        print("wrong choice")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")




