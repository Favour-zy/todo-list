def todo_list():
    tasks = []

    while True:
        print("\n=== To-Do List ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append({"task": task, "completed": False})
            print("Task added successfully!")

        elif choice == "2":
            if not tasks:
                print("No tasks in the list!")
            else:
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["completed"] else " "
                    print(f"{i}. [{status}] {task['task']}")

        elif choice == "3":
            if not tasks:
                print("No tasks to mark as complete!")
            else:
                task_num = int(input("Enter task number to mark as complete: ")) - 1
                if 0 <= task_num < len(tasks):
                    tasks[task_num]["completed"] = True
                    print("Task marked as complete!")
                else:
                    print("Invalid task number!")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

todo_list()