from models.Manager import Manager as mege

Manager = mege()
while True:
    print('''1 - add task
2 - remove task
3 - list task
4 - exit''')
    choice = input('Choice> ')
    if choice == '1':
        Manager.AddTask()
    elif choice == '2':

        Manager.DeleteTask()
    elif choice == '3':
        Manager.list_tasks()
    else:
        Manager.Sobreescrever_arquivo()
        break