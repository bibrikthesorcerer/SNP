# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

import datetime

def date_in_future(days: int=0):
    """
    Returns a string representing the date and time in the future by the specified number of days.
    """
    # если подали не целое число - будем возвращать текущую дату
    if not isinstance(days, int) :
        days = 0
    # получить дату через days дней
    date = datetime.datetime.now() + datetime.timedelta(days=days)
    # вернуть отформатированную дату
    return date.strftime("%d-%m-%Y %H:%M:%S")
