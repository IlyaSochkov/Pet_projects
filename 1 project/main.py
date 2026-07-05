import json

def read_tasks(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("Файла нет, создам новый.")
        data = {'tasks':[]}
    return data

def update_tasks(data, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_task(title, tasks):
    title = title.split(", ")

    if tasks["tasks"]:
        new_id = tasks["tasks"][-1]["id"] + 1
    else:
        new_id = 1

    task_title = title[0] if len(title) > 0 else ''
    task_tags = title[1:] if len(title) > 1 else []
    tasks["tasks"].append({
        "id": new_id,
        "title": task_title,
        "tags": task_tags,
        "done": False
    })

def list_tasks(tasks, filter_tag=None):
    print("|id|title|tags|done")
    for task in tasks["tasks"]:
        print(f"| {task['id']} | {task['title']} | {task['tags']} | {task['done']} |")

file_name = "tasks.json"

data = read_tasks(file_name)
print(data)
new_task = input("Введи новою задачу: ")
add_task(new_task, data)
update_tasks(data, file_name)
list_tasks(data)