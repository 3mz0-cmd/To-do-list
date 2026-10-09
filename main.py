tasks = {}

def menu():
    print("To-do List App")
    print("1.Add a Task")
    print("2.Remove a Task")
    print("3.Mark task as done")
    print("4.View Tasks")
    print("5.Quit")

def add_task():
    add_input = input("Enter your task:\n").capitalize()
    if not add_input:
        print("Please enter a task!")
    elif add_input in tasks:
        print("This task was already added!\n")
    else:
        status = False
        tasks[add_input] = status
        save_tasks()
        print("Successfully added a task!\n")

def remove_task():
    if not tasks:
        print("Your to-do list is empty\n")
    else: 
        remove_input = input("Which task do you want to remove?\n").capitalize().strip()
        if remove_input in tasks:
            tasks.pop(remove_input)
            save_tasks()
            print("Successfully removed a task!\n")
        else: 
            print("This task isn't in your to-do list\n")

def complete_tasks():
    if not tasks:
        print("Your to-do list is empty.\n")
    else:
        complete_input = input("Which task have you completed?\n").capitalize().strip()

        if complete_input not in tasks:
            print("This task is not in your to-do list.\n")

        elif tasks[complete_input] == True:
            print("This task is already completed.\n")
        elif tasks[complete_input] == False:
            tasks[complete_input] = True
            save_tasks()
            print(f"You've completed '{complete_input}'\n")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty\n")
    else:
        print("Your tasks:")
        for i, (task , status) in enumerate(tasks.items(), start=1):
            if status:
                status_text = "Complete!"
            else:
                status_text = "Pending..."
            print(f"{i}. {task} | Status: {status_text}")
        print("Successfully viewed your tasks!\n")

def save_tasks():
    with open("to-do_list.txt" , "w") as file:
        for task , status in tasks.items():
            file.write(task +" | " + str(status) + "\n")

def load_tasks():
    try:
        with open("to-do_list.txt", "r") as file:
            for line in file:

                parts = line.split("|")
                task = parts[0].strip()
                status = parts[1].strip() == "True"

                tasks[task] = status

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
            complete_tasks()
            continue
        elif option == "4":
            view_tasks()
            continue
        elif option == "5":
            print("Goodbye!")
            break
        else: 
            print("Invalid  option. Choose from 1-5 only!\n")
            continue
app()
