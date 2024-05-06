# Author: Ignat Sakhovsky
# Email: ignatsahovsky@gmail.com

import datetime

def date_in_future(days=0):
    """
    Returns a string representing the date and time in the future by the specified number of days.
    
    Parameters:
        days (int) = 0: The number of days in the future. Default is 0.
        
    Returns:
        str: A string representing the date and time in the format "%d-%m-%Y %H:%M:%S".
    """
    date = datetime.datetime.now() + datetime.timedelta(days=days)
    return date.strftime("%d-%m-%Y %H:%M:%S")
