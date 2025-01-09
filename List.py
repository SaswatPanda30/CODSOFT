class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def __str__(self):
        status = "Y" if self.completed else "X"
        return f"[{status}] {self.title}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f'Task "{title}" added to the list.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nTo-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self, index, new_title):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = new_title
            print(f'Task {index + 1} updated to "{new_title}".')
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task "{removed_task.title}" removed from the list.')
        else:
            print("Invalid task number.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f'Task "{self.tasks[index].title}" marked as completed.')
        else:
            print("Invalid task number.")


def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            title = input("Enter the task title: ")
            todo_list.add_task(title)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to update: ")) - 1
                new_title = input("Enter the new task title: ")
                todo_list.update_task(task_number, new_title)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.mark_completed(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '6':
            print("Exiting the To-Do List application")
            break
        else:
            print("Invalid ! Please select a valid option.")


if __name__ == "__main__":
    main()
