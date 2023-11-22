from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create or select a database
db = client['task_manager']

# Create collections for tasks and projects
tasks_collection = db['tasks']
projects_collection = db['projects']

# CRUD operations for tasks
def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    project_id = input("Enter project ID for the task (or press Enter for no project): ")
    due_date_str = input("Enter due date for the task (YYYY-MM-DD) or press Enter: ")

    due_date = None
    if due_date_str:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')

    task_data = {
        'title': title,
        'description': description,
        'project_id': project_id,
        'due_date': due_date,
        'status': 'To Do',
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }
    result = tasks_collection.insert_one(task_data)
    print(f"Task created with ID: {result.inserted_id}")

def read_tasks():
    tasks = tasks_collection.find()
    return list(tasks)

# CRUD operations for projects
def create_project():
    name = input("Enter project name: ")
    description = input("Enter project description: ")

    project_data = {
        'name': name,
        'description': description,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }
    result = projects_collection.insert_one(project_data)
    print(f"Project created with ID: {result.inserted_id}")

def read_projects():
    projects = projects_collection.find()
    return list(projects)

# Other CRUD operations remain unchanged

# Example usage
create_project()
create_task()

projects = read_projects()
print("\nAll Projects:")
for project in projects:
    print(f"{project['_id']} - {project['name']} - {project['description']}")

tasks = read_tasks()
print("\nAll Tasks:")
for task in tasks:
    print(f"{task['_id']} - {task['title']} in project {task['project_id']} - Status: {task['status']}")
