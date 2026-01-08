from app.database import create_table, connect

def add_task(title):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()
    print("Task added.")

def list_tasks():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "DONE" if task[2] else "TODO"
        print(f"{task[0]}. {task[1]} [{status}]")

def complete_task(task_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print("Task completed.")

def main():
    create_table()  # Създава таблицата, ако не съществува

    while True:
        print("\n1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = input("Task ID: ")
            complete_task(task_id)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
