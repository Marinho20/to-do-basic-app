Task = tuple[int, str, str] ## Define a Task as a tuple of (id, title, status)
tasks= list[Task]           

tasks = []


def add_task():
    title = input("Enter task title: ")
    id = len(tasks) +1
    for Task in tasks:
       if title == Task[1]:
        print("task already exists")
        return
       elif title.strip() == "":
        print("task title cannot be empty")
        return
    tasks.append((id, title, "Pending"))
    print(f"Task {title} added with ID {id}.")  
        
    

def remove_task():
    view_tasks()
    if len(tasks) == 0:
        print("No tasks to remove.")
        return
    else:
        id_remove = int(input("Enter task ID to remove: "))
        for task in tasks:
            if task[0] == id_remove:
                tasks.remove(task)
                print(f"Task {task[1]} removed from the list.")
                return
        print("Task ID not found.")
        
            


def view_tasks():
    if len(tasks) == 0:
            print("No tasks available.")
            return
    else :
        print("Tasks: ")
        for task in tasks:
         print(f"ID: {task[0]}, Title: {task[1]}, Satus: {task[2]}")



def update_id():
    i = 0
    for task in tasks:
        i += 1
        tasks[i-1] = (i, task[1], task[2])



def save_file():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task[0]},{task[1]},{task[2]}\n")

def load_file():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                id_str, title, status_ = line.strip().split(",", 2)
                tasks.append((int(id_str), title, status_))
    except FileNotFoundError:
        print("No saved tasks found.")


def mark_complete():    
    view_tasks()
    if len(tasks) == 0:
        print("No tasks to mark as complete.")
        return
    else:
        id_complete = int(input("Enter task ID to mark as complete: "))
        for i, task in enumerate(tasks):
            if task[0] == id_complete:
                tasks[i] = (task[0], task[1], "Complete")
                print(f"Task {task[1]} marked as complete.")
                return
        print("Task ID not found.")


def clear_completed_tasks():
    for task in tasks:
        contador = 0
        if task[2] == "Complete":
            tasks.remove(task)
            print(f"task {task[1]} removed from the list.")
            contador += 1
    print(f" {contador} completed tasks have been cleared.")



