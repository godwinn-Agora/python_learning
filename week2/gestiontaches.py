print("WELCOME TO THE TASK MANAGER !")

tasks = []

while True:
    print("\nMenu :")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. Display tasks")
    print("4. Features")
    print("5. Quit")
    choice = input("Choose an option (1-4) : ")

    if choice == '1':
        task = {"name": input("Enter the task name : "), "completed": False}
        name = task["name"]
        tasks.append(task)
        print(f"Task '{name}' added.")
    elif choice == '2':
        name = input("Enter the task to delete : ")
        for task in tasks:
            if task["name"] == name:
                tasks.remove(task)
                print(f"Task '{name}' deleted.")
                break
        else:
            print(f"Task '{name}' not found.")
    elif choice == '3':
        print("List of tasks :")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    elif choice == '4':
        name = input("which task's features do you want to see ?")
        for task in tasks:
            if task["name"] == name:
                print(task)
                choice = input("Which features do you want to change ?")
                if choice.lower() == "name":
                    task["name"] = input("Write the new name of your task:")
                    print(task)
                elif choice.lower() == "completion":
                    completion = input("Do you have completed the task ?")
                    for task in tasks:
                        if completion.lower() == "yes":    
                            task["completed"] = True
                        elif completion.lower() == "no":
                            task["completed"] = False
                        else:
                            print("Answer by yes or no !")
                    break
                break
        else:
            print(f"Task '{name}' not found.")         
    elif choice == '5':
        print("Goodbye !")
        break
    else:
        print("Invalid option, please try again.")

