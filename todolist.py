# Simple To-Do List 

tasks = ["study python", "complete assignment"]

print("TO-DO LIST")
print("1. Add Task")
print("2. View Tasks")
print("3. Remove Task")

choice = input("Enter your choice: ")

if choice == "1":
    task = input("Enter new task: ")
    tasks.append(task)
    print("you have choosed option 1 to add an task")
    print("Task added successfully.")

elif choice == "2":
    print("Your Tasks:")
    for i in range(len(tasks)):
        print(i+1, ".", tasks[i])

elif choice == "3":
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("you have choosen 3 option to remove task successfully")
        print("Task removed successfully.")
    else:
        print("Task not found.")

else:
    print("Invalid choice.")