import json
import os

class Task:
    def __init__(self,task_id,title,description,status):
        self.task_id=task_id
        self.title=title
        self.description=description
        self.status='pending'

    def mark_completed(self):
        self.status='completed'
    def display(self):
        print("\n-----------------------------")
        print("task id   :",self.task_id)
        print("title     :",self.title)
        print("description:",self.description)
        print("status     :",self.status)
        print("--------------------------------")
class TodoManager:
    def __init__(self,filename='taskjson'):
        self.tasks=[]
        self.filename=filename
        self.load_tasks()
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename,"r") as file:
                    data=json.load(file)

                for item in data:
                    task=Task(item["task_id"],
                              item["title"],
                              item["description"],
                              item["status"])
                    self.tasks.append(task)
            except(json.JSONDecodeError,KeyError,TypeError):
                    print("warning:saved task data could not be loaded.")
    def save_tasks(self):
        data=[]
        for task in self.tasks:
            data.append({
                "task_id":task.task_id,
                "title":task.title,
                "Description":task.description,
                "status":task.status
                })
            with open(self.filename,"w") as file:
                json.dump(data,file,indent=4)
    def find_task(self,task_id):
        for task in self.tasks:
            if task.task_id==task_id:
                return task
        return None
    def add_task(self):
        title=input("enter Title:").strip()
        description=input("enter description:").strip()
        status="pending"

        if not title:
            print("title cannot be empty")
            return
        if self.tasks:
            task_id=max(Task.task_id for task in self.tasks)+1
        else:
            task_id=1
        new_task=Task(task_id,title,description,status)
        self.tasks.append(new_task)
        self.save_tasks()

        print("task added successfully!")
        print("your Task id is:",task_id)
    def display(self):
        if not self.tasks:
            print("no tasks available")
            return
        for task in self.tasks:
            print(task.task_id,task.title,task.description,task.status)
                          
    def view_tasks(self):
        if not self.tasks:
            print("no tasks available.")
            return
        for task in self.tasks:
            task.display()
    def search_task(self):
        try:
            task_id=int(input("enter Task_id to search:"))
        except ValueError:
            print("please enter a valid numeric ID.")
            return
        task=self.find_task(task_id)
        if task:
            task.display()
        else:
            print("task not found!")
    def update_task(self):
        try:
            task_id = int(input("Enter Task ID to update: "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        task = self.find_task(task_id)

        if task is None:
            print("Task Not Found!")
            return

        print("Leave a field blank to keep its current value.")

        title = input("Enter New Title: ").strip()
        description = input("Enter New Description: ").strip()

        if title:
            task.title = title

        if description:
            task.description = description

        self.save_tasks()
        print("Task Updated Successfully!")
    
    def delete_task(self):
        try:
            task_id = int(input("Enter Task ID to delete: "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        task = self.find_task(task_id)

        if task is None:
            print("Task Not Found!")
            return

        self.tasks.remove(task)
        self.save_tasks()

        print("Task Deleted Successfully!")
    def mark_completed(self):
        try:
            task_id = int(input("Enter Task ID to complete: "))
        except ValueError:
            print("Please enter a valid numeric ID.")
            return

        task = self.find_task(task_id)

        if task is None:
            print("Task Not Found!")
            return

        task.mark_completed()
        self.save_tasks()

        print("Task Marked as Completed!")
def main():
        manager = TodoManager()

        while True:
            print("\n===== TODO APPLICATION =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Search Task")
            print("4. Update Task")
            print("5. Delete Task")
            print("6. Mark Completed")
            print("7. Exit")

            choice = input("Enter Choice: ").strip()

            if choice == "1":
                manager.add_task()

            elif choice == "2":
                manager.view_tasks()

            elif choice == "3":
                manager.search_task()

            elif choice == "4":
                manager.update_task()

            elif choice == "5":
                manager.delete_task()

            elif choice == "6":
                manager.mark_completed()

            elif choice == "7":
                print("Thank you for using TODO Application!")
                break

            else:
                print("Invalid choice! Please select 1 to 7.")


if __name__ == "__main__":
    main()
            
