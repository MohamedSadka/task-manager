

tasks = [{"task":"Quran", "completed":True}, {"task":"Salah", "completed":True}, 
        {"task":"Study", "completed":False}, {"task":"Exercise", "completed":True}, 
        {"task":"Sleep", "completed":False}, {"task":"Visit Hamada", "completed":True}
    ]

def main():

    message = """
1- add task to list
2- mark task as complete
3- view tasks
4- quit the program
"""

    while True:
        print(message)
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
            
        elif choice == "2":
            mark_task_complete(choice)
        
        elif choice == "3":
            view_tasks(tasks)
            
        elif choice == "4":
            break
        else:
            print("Invalid choice , choose a number between 1 and 4")


def add_task():
    # get task from the user
    task = input("What do you want to do: ")
    # define the status of the task
    task_info = {"task":task , "completed":False}
    #add task to the takss
    tasks.append(task_info)
    print(f"{task} has been added successfully")
    

def mark_task_complete(task):
    # get list of incompleted tasks
    incompleted_tasks = [task for task in tasks if task["completed"] == False]

    if not incompleted_tasks:
        print("no tasks to mark as complete")
        return
    # show them to the user
    for index,task in enumerate(incompleted_tasks,1):
        print(f"{index}. {task['task']}: {task['completed']}")
        print("-" * 20)
    
    try:
        # get the task from the user
        task_number = int(input("Enter the number of the task: "))

        if task_number < 0 or task_number > len(incompleted_tasks):
            print("Enter a number from the list")
            return
        # # make it as completed
        incompleted_tasks[task_number - 1]["completed"] = True
        print("Task has marked completed")
    except ValueError:
        print("invalid choice, please enter a number")

def view_tasks(task_list):
    if not task_list:
        print("no tasks found")
        return
    
    for i, task in enumerate(task_list):
        status = "✔" if task['completed'] else '❌'
        print(f"{i+1}. {task['task']}: {status}")

if __name__ == "__main__":
    main()

