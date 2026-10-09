tasks = {}

def menu():
    print("To-do List App")
    print("1.Add a Task")
    print("2.Remove a Task")
    print("3.View Tasks")
    print("4.Quit")

def add_task():
    add_input = input("Enter your task:\n")
    if add_input in tasks:
        print("This task was already added!\n")
    else:
        tasks.append(add_input)
        print("Successfully added a task!\n")

def remove_task():
    if not tasks:
        print("Your to-do list is empty\n")
    else: 
        remove_input = input("Which task do you want to remove?\n")
        if remove_input not in tasks:
            print("This task isn't in your to-do list\n")
        else: 
            tasks.remove(remove_input)
            print("Successfully removed a task!\n")
        
def view_tasks():
    if not tasks:
        print("Your to-do list is empty\n")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("Successfully viewed your tasks!\n")

def save_tasks():
    with open("to-do_list.txt" , "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("to-do_list.txt" , "r") as file:
            for task in file:
                task = task.strip()
                tasks.append(task)
    except FileNotFoundError:
        pass

def app():
    load_tasks()

    while True:
        menu()
        option = input("Enter your option: ")

        if option == "1":
            add_task()
            continue
        elif option == "2":
            remove_task()
            continue
        elif option == "3":
            view_tasks()
            continue
        elif option == "4":
            save_tasks()
            print("Goodbye!")
            break
        else: 
            print("Invalid  option. Choose from 1-4 only!")
            continue
app()