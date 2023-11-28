todo = {}
def add():
    task_name = input('Enter the name of the task: ')
    status = input('Enter the status of the task (Complete/Incomplete): ')
    p = input('Enter the priority of the task (High/Medium,Low): ')
    todo[task_name] = f'Status - {status} Priority - {p}'

def view():
    if not todo:
        print('No tasks found.')
    else:
        for item, status in todo.items():
            print(f'Task: {item} - Status: {status}')
def remove():
    r = input('Enter the name of the item you want to remove: ')
    if r.lower() in todo:
        todo.pop(r)
    else:
        print('Invalid Input')
def delete():
    if not todo:
        print('No tasks to delete.')
    else:
        view()
        item = input('Enter the task to delete: ')
        if item in todo:
            del todo[item]
            print(f'Task "{item}" deleted successfully!')
        else:
            print('Task not found')

def c():
    t = input('Enter the name of the task you want to mark: ')
    h = input('Enter the current status (Complete/Incomplete):')
    if t in todo.keys():
        value = 'Status- ' + str(h)
        todo[t] = value
    else:   
        print('Invalid input')
while True:
    print('1. Add task')
    print('2. Delete task')
    print('3. View task')
    print('4. Mark complete or incomplete')
    print('5. Exit')
    k = input('Choose your choice (1-5): ')
    if k == str(1):
        add()
    elif k == str(2):
        remove()
    elif k == str(3):
        view()
    elif k == str(4):
        c()
    elif k == str(5):
        break
    else:
        print('Invalid input')
