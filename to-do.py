# Define a list to store tasks
tasks = []

# Define a function to display the menu


def display_menu():
    print('Todo List Menu:\n')
    print('1. Add Task')
    print('2. Mark Task as Complete')
    print('3. View Tasks')
    print('4. Save file')
    print('5. Load file')
    print('6. Quit\n')

# Define a function to add a task to the list


def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "complete": False})
    print("Task added successfully!")

# Define a function to mark a task as complete


def mark_task_complete():
    if not tasks:
        print("No tasks available to mark as complete.")
        return

    print("Tasks:")
    for i, task in enumerate(tasks):
        print(
            f"{i + 1}. {task['task']} ({'Complete' if task['complete'] else 'Incomplete'})")

    task_number = input("Enter the number of the task to mark as complete: ")

    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            task['complete'] = True
            print(f"Task '{task['task']}'  completed.\n")
        else:
            print("Invalid task number. Please enter a valid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.\n")
        
# Define a function to view tasks

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['task']} ({'Complete' if task['complete'] else 'Incomplete'})")


# Define a function to save tasks to a file
def save_to_file():
    file_name = input("Enter the file name to save tasks: ")

    try:
        with open(file_name, 'w') as file:
            for task in tasks:
                file.write(
                    f"{task['task']} ({'Complete' if task['complete'] else 'Incomplete'})\n")

        print("Tasks saved to file successfully!\n")
    except Exception as e:
        print(f"Error saving tasks to file: {str(e)}")


# Define a function to load tasks from a file
def load_from_file():
    file_name = input("Enter the file name to load tasks from: ")

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            # Clear existing tasks
            tasks.clear()

            for line in lines:
                parts = line.strip().split(' (')
                task_description = parts[0]
                task_status = parts[1][:-1]  # Remove the closing parenthesis

                tasks.append({"task": task_description,
                             "complete": task_status == 'Complete'})

        print("Tasks loaded from file successfully!\n")
    except Exception as e:
        print(f"Error loading tasks from file: {str(e)}")
        
# Define the main program loop

def main():
    while True:
        display_menu()
        choice = input('Enter your Choice: ')

        if choice == '1':
            add_task()
        elif choice == '2':
            mark_task_complete()
        elif choice == '3':
            # Call the function to view tasks
            view_tasks()
        elif choice == '4':
            save_to_file()   # Call the function to save a file
            pass
        elif choice == '5':
            # Call the function to load a file
           load_from_file() 
        elif choice == '6':
            print('Goodbye.\n')
            break  # Exit the program
        else:
            print('Invalid choice. Please try again.')


# Entry point of the program
if __name__ == "__main__":
    main()
