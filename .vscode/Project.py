import os

FILE_NAME="Tasks.txt"
#load to task
def load_tasks():
    tasks={}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            for line in file:
                task_id,title,status=line.strip().split(" | ")
                tasks[int(task_id)]={"title":title,"status": status}
            
    return tasks

#save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME,"w") as file:
        for task_id,task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")


# add a new task
def add_task(tasks):
    title=input("Enter title to add a task : ")
    task_id=max(tasks.keys(),default=0)+1
    tasks[task_id]={"title":title,"status":"incomplete"}
    print(f"Task {title} added.")

# view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        for task_id,task in tasks.items():
          print(f"[{task_id}] {task['title']} - {task['status']}")

# mark task as complete
def mark_as_complete(tasks):
    task_id=int(input("Enter task ID to mark as complete :"))
    if task_id in tasks:
        tasks[task_id]["status"]="complete"
        print(f"Task '{tasks[task_id]['title']}' marked as completed")
    else:
        print("Task ID not found ")
# delete task
def delete_task(tasks):
    task_Id=int(input("Enter task ID to Delete : "))
    if task_Id in tasks:
        deleted_task=tasks.pop(task_Id)
        print(f"Task '{deleted_task['title']}' deleted")
    else:
        print("Task ID not found ")

def main():
     tasks=load_tasks()
     while True:
         print("\nMain Menu of Task Manager ")
         print("1. add task")
         print("2. view tasks")
         print("3. mark task as complete")
         print("4. Delete task")
         print("5. Exit ")

         choice=int(input("Enter your choice : "))

         if choice==1:
             add_task(tasks)
         elif choice==2:
             view_tasks(tasks)
         elif choice ==3:
             mark_as_complete(tasks)
         elif choice ==4:
             delete_task(tasks)
             save_tasks(tasks)
             print("Goodbye")
             break
         else:
             print("INVALID CHOICE !!, Please try again")

if __name__ == "__main__":
    main()
