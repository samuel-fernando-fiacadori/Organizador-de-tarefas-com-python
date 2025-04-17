import datetime

class ProcessInfo:
    @classmethod
    def Complete(cls, completed: bool):
        return 'completed' if completed else 'incompleted'
    @classmethod
    def date_time_remaing(cls, date: str):
        try:
            
            today_time: datetime.date = datetime.date.today()
            splited_date = date.split('/')

            if int(splited_date[0]) >= today_time.day and int(splited_date[1]) >= today_time.month:
                return f'{int(splited_date[0]) - today_time.day} days and {int(splited_date[1]) - today_time.month} months remaing'
            return 'this task date already passed!'

        except ValueError:
            raise ValueError('The givven date are wrong, please try again')

    @classmethod
    def situation_task(cls, processed_complete: str, processed_date: str):
        return f'task situation: {processed_complete}, {processed_date if not processed_complete == 'completed' else 'already completed'}'