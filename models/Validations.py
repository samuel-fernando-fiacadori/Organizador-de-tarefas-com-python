import re, datetime

class ValidationClass:
    @classmethod
    def Validate_Name(cls, name) -> str: # just put here the expected output type
        if not name:
            raise ValueError("the task MUST have a name, certifycate you don't will forgot this.")
        return name
    @classmethod
    def Validate_Description(cls, description: str) -> str:
        if not description:
            return 'None description added'
        return description
    @classmethod
    def Validate_Date(cls, date: str) -> str:
        if date.lower() == 'today':
            return f'{datetime.datetime.today().day}/{datetime.datetime.today().month}/{datetime.datetime.today().year}'
        regex = re.compile(r'([0-9]{1,2}[/][0-9]{1,2}[/][0-9]{4})')
        if regex.match(date):
            return date
        raise ValueError(f'The date must be padronized (dd/mm/aaaa)')