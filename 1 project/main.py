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

def add_task(title, file_name):
    tasks = read_tasks(file_name)
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
    update_tasks(tasks, file_name)


def list_tasks(file_name, filter_tag=None):
    tasks = read_tasks(file_name)
    print("|id|title|tags|done")
    for task in tasks["tasks"]:
        print(f"| {task['id']} | {task['title']} | {task['tags']} | {task['done']} |")

def done_task(file_name, task_id):
    tasks = read_tasks(file_name)
    for task in tasks["tasks"]:
        if task['id'] == task_id:
            task['done'] = True
            break
    update_tasks(tasks, file_name)

def delete_task(file_name, title):
    tasks = read_tasks(file_name)
    for task in tasks["tasks"]:
        if task['id'] == task_id:
            tasks["tasks"].remove(task)
            break
    update_tasks(tasks, file_name)

def clean(file_name):
    data = {'tasks':[]}
    update_tasks(data, file_name)

file_name = "tasks.json"

while True:
    print("Есть набор команд:" \
    "\n 1. Добавить дело - add" \
    "\n 2. Удалить дело по названию - delete" \
    "\n 3. Отметить дело сделанным - done" \
    "\n 4. Отчистить список - clean" \
    "\n 5. Вывести список - list")

    command = input("Введи команду: ").strip().lower()
        
    match command:
        case "list":
            list_tasks(file_name)
        case "add":
            title = input("Введи новую задачу: ")
            add_task(title, file_name)
        case "done":
            task_id = int(input("Введи ID задачи: "))
            done_task(file_name, task_id)
        case "delete":
            task_id = int(input("Введи ID задачи: "))
            delete_task(file_name, task_id)
        case "clean":
            clean(file_name)
            print("Выполненные задачи удалены!")
        case "exit":
            print("До свидания!")
            break
        case _:
            print("Неизвестная команда!")