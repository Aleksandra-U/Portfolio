

from datetime import datetime


def intTry(value):
    try:
        your_num = int(value)
        return True
    except ValueError:
        return False
    


def getting_date():

    while True:
        year = input('Enter the year:')
        month = input('Enter the month:')
        day = input('Enter the day:')

        try:
            return datetime(int(year), int(month), int(day))
        except Exception as e:
            pass



def check_future():
    my_date = getting_date()

    today = datetime.now()

    try_future = today - my_date

    return try_future.days




    
#start
def your_birthday():
    user_date = check_future()

    while user_date < 0:
        print('Error. You entered a date from the future')

        user_date = check_future()

    print(user_date)



your_birthday()