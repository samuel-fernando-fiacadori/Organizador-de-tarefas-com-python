from models.Validations import ValidationClass # Nome mais específico
from models.ProcessInfo import ProcessInfo

class Tarefa:
    '''this object function is: offer organazation for user'''

    def __init__(self, name: str, description: str, date: str, complete: bool) -> None:
        self._name: str = ValidationClass.Validate_Name(name) # Correção da chamada e do nome
        self._description: str = ValidationClass.Validate_Description(description) # Correção da chamada e do nome
        self._date: str = ValidationClass.Validate_Date(date) # Correção da chamada e do nome
        self._complete: bool = complete

    def __repr__(self) -> str: # root information
        return f'Name: {self._name}\nDate: {self._date}\nDescription: {self._description}\nSituation: {"completed" if self._complete else "incompleted"}\n'

    def __str__(self) -> str: # processed information
        return f'''
        ===TASK===
        name: {self._name}
        description: {self._description}
        date: {self._date}

        {ProcessInfo.situation_task(ProcessInfo.Complete(self._complete), ProcessInfo.date_time_remaing(self._date))}
        '''