from .ModelTarefa import Tarefa
import json
import os
class DataManager:
    @classmethod
    def Sobreescrever(cls, list_task: list[Tarefa]):
        with open('data/Tasks.txt', 'w') as archive:
            task_data = []
            for task in list_task:
                # Converta o objeto Tarefa para um dicionário
                task_dict = {
                    'name': task._name,
                    'description': task._description,
                    'date': task._date,
                    'complete': task._complete,
                }
                task_data.append(task_dict)  # Adicione o dicionário à lista
            json.dump(task_data, archive, indent=4)  # Salve a lista de dicionários em JSON
    @classmethod
    def Interpretar(cls, lista: list[str]):
        if not len(lista) == 4:
            return ''
        good_info = []
        for i in range(len(lista)):
            variable_i_need = lista[i].split(' ')[1]
            good_info.append(variable_i_need)
        return good_info
    
    @classmethod
    def Read(cls) -> list[Tarefa]:
        tasks = []
        try:
            with open('data/Tasks.txt', 'r') as archive:
                task_data = json.load(archive)  # Carregue os dados JSON do arquivo
                for task_dict in task_data:
                    # Crie objetos Tarefa a partir dos dicionários
                    tasks.append(
                        Tarefa(
                            task_dict['name'],
                            task_dict['description'],
                            task_dict['date'],
                            task_dict['complete'],
                        )
                    )
        except FileNotFoundError:
            # Se o arquivo não existir, retorne uma lista vazia
            # Isso evita um erro se o programa for executado pela primeira vez
            return []
        return tasks

class Manager:
    def __init__(self):
        self._list_task = DataManager.Read()
    
    def Sobreescrever_arquivo(self):
        DataManager.Sobreescrever(self._list_task)

    def AddTask(self):
            Name: str = input('Write the task name> ')
            Description: str = input('Write the task description (optional)> ')
            Date: str = input('Write the finalyzanting date (dd/mm/aaaa) hint: Write today for using today date> ')
            try:
                newTask = Tarefa(Name, Description, Date, False)
                self._list_task.append(newTask)
                self.Sobreescrever_arquivo() # Salvar as alterações no arquivo
                print('Tarefa adicionada com sucesso!')
            except ValueError as e:
                print(f'Erro ao adicionar tarefa: {e}')
            except Exception as e: # Para outros erros inesperados
                print(f'Ocorreu um erro inesperado: {e}')
            input('Press enter to exit')
            os.system('cls')
    
    def DeleteTask(self):
        Task_name_or_index: str | int = input('Write the task name or his index> ')
        try:

            self._list_task.pop(int(Task_name_or_index))
            print('The task was removed with sucefully')
            self.Sobreescrever_arquivo()
        except IndexError:
            for task in self._list_task:
                if task._name == Task_name_or_index:
                    self._list_task.pop(self._list_task.index(task))
        input('Press enter to exit')
        os.system('cls')

    def list_tasks(self):
        for task in self._list_task:
            print(task.__repr__())
        input('Press enter to exit')
        os.system('cls')
