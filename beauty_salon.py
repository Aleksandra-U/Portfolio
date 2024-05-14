


import os
import pandas as pd
from datetime import datetime, date

class Services():
    def __init__(self, type, price, how_long):
        self.type = type
        self.price = price
        self.how_long = how_long

class Masters():
    def __init__(self, name, age, gender, type_servisces): 
        self.name = name
        self.age = age
        self.gender = gender
        self.type_servisces = type_servisces 

class Nail_polish():
    def __init__(self, color, type, exp_date):
        self.color = color
        self.type = type
        self.expiration_date = exp_date

class Salon():
    def __init__(self, list_masters, list_nail_polish):
        self.list_mas = list_masters
        self.list_nail_polish = list_nail_polish

    def add_mas_to_list(self, name, age, gender, type_servisces):
        mas1 = Masters(name, age, gender, type_servisces)

        self.list_mas.append(mas1)   



    def add_nail_polish_to_list(self, color, type, expiration_date):
        nail_polish1 = Nail_polish(color, type, expiration_date)   

        self.list_nail_polish.append(nail_polish1)


    def save_nail_polish_mas_ser_to_df_to_csv(self):
        df_nail_polish = []
        for my_nail_polish in self.list_nail_polish:
            under_df_nail_polish = (my_nail_polish.color, my_nail_polish.type, my_nail_polish.expiration_date) 
            df_nail_polish.append(under_df_nail_polish)
        my_df_nail_polish = pd.DataFrame(df_nail_polish,columns=['color', 'type', 'expiration_date'])    
        my_df_nail_polish.to_csv('my_nail_polish.csv', index=False)


        df_mas = []
        for my_mas in self.list_mas:
            under_df_mas = (my_mas.name, my_mas.age, my_mas.gender) 
            df_mas.append(under_df_mas)
        my_df_mas = pd.DataFrame(df_mas,columns=['Name', 'age', 'gender'])    
        my_df_mas.to_csv('my_mas.csv', index=False)


        df_ser = []
        for my_ser in self.list_mas:
            for type_ser in my_ser.type_servisces:
                under_df_ser = (my_ser.name,type_ser.type, type_ser.price, type_ser.how_long) 
                df_ser.append(under_df_ser)
            my_df_ser = pd.DataFrame(df_ser,columns=['name_mas','type','price','how_long'])    
            my_df_ser.to_csv('my_ser.csv', index=False)



    def to_list_nail_polish_mas_from_csv(self):
        df_mas = pd.read_csv('my_mas.csv')
        df_ser = pd.read_csv('my_ser.csv')
        for index, row in df_mas.iterrows(): 
            name = row.Name
            age = row.age
            gender = row.gender


            type_servisces = []
            for index, row in df_ser.iterrows(): 
                
                name_mas = row.name_mas
                type = row.type
                price = row.price
                how_long = row.how_long

                if name == name_mas:
                    service = Services(type, price, how_long)
                    type_servisces.append(service)

            my_mas = Masters(name, age, gender, type_servisces)

            self.list_mas.append(my_mas)



        df = pd.read_csv('my_nail_polish.csv')
        for index, row in df.iterrows(): 
            color = row.color
            type = row.type
            expiration_date = row.expiration_date

            my_nail_polish = Nail_polish(color, type, expiration_date)

            self.list_nail_polish.append(my_nail_polish)


    def print_all_mas(self):
            
            print('available_masters: ')
            for every_mas in self.list_mas:
                print(f'\n {every_mas.name}:')
                num_ser = 1
                for ser in every_mas.type_servisces:
                    print(f'{num_ser}. Service: {ser.type}, Price: ${ser.price}, Duration of the procedure: {ser.how_long} min')
                    num_ser+=1

    def print_all_ser(self):
        num_ser = 1
        for my_mas in self.list_mas: 
            for type_ser in my_mas.type_servisces:
                print((f'{num_ser}. Service: {type_ser.type}, Price: ${type_ser.price}, Duration of the procedure: {type_ser.how_long} min'))
                num_ser += 1


    def print_all_nail_polish(self):
        print('Nail polish that are available: ')
        for every_nail_polish in self.list_nail_polish:
            print(f'The color of the nail polish: {every_nail_polish.color}, Type of nail polish: ${every_nail_polish.type}, Expiration date: {every_nail_polish.expiration_date}')   
    






my_salon = Salon([], [])

service1 = Services('manicure', 2000, 90) 
service2 = Services('haircut', 4000, 60)
service3 = Services('haircut', 1000, 180)
service4 = Services('manicure', 500, 240)

my_salon.add_mas_to_list('Nina', 35, 'female', [service1, service2])
my_salon.add_mas_to_list('Maxim', 16, 'male', [service3, service4])
my_salon.add_mas_to_list('Oleg', 27, 'male', [service2])
my_salon.add_mas_to_list('Sveta', 22, 'female', [service1])

my_salon.add_nail_polish_to_list('blue', 'shellac', datetime(2025,5,2)) #сюда добавить datetime
my_salon.add_nail_polish_to_list('pink', 'ordinary', datetime(2025,3,12))




def try_int_which_num(value):
    possible_num = range(1, 8)
    try:
        your_num = int(value)
        if your_num in possible_num:
            return True
        else:
            print('Please, enter a number from 1 to 7')
            return False
    except Exception as e:
        print('Please, enter a number from 1 to 7')
        return False


def which_operation():
    whats_the_operation = input('What kind of operation would you like to perform?\n'
                                    '1. Add nail polish \n'
                                    '2. Write a list of nail polish, services and masters in a CSV-file \n'
                                    '3. Download a list of nail polish, masters and services from a CSV-file \n'
                                    '4. Show a list of all available masters \n'
                                    '5. Show a list of all available services \n'
                                    '6. Show the list of nail polish available \n'
                                    '7. Exit the menu \n'
                                    'Please, select a number 1, 2, 3, 4, 5, 6 or 7: ' )
    return whats_the_operation



def start_program():

    while True:
        preferred_operation = which_operation()

        check_int_num = try_int_which_num(preferred_operation)
        check_int_num = False
        while check_int_num == False: 
            preferred_operation = which_operation()
            check_int_num = try_int_which_num(preferred_operation)


        add_nail_polish = '1'
        to_scv = '2'
        from_scv = '3'
        show_masters = '4'
        show_services = '5'
        show_nail_polish = '6'
        exit = '7'
        

        if preferred_operation == add_nail_polish:
            clear = lambda: os.system('cls')
            clear()

            input_color = input('What color nail polish would you like to add?: ')
            input_type = input('What type of nail polish would you like to add: shellac, ordinary nail polish?: ')

            your_date = 0
            while True:
                input_date = input('What is the expiration date of this nail polish: ')
                expiration_da = input_date 

                try:
                    day = int(input_date.split('.')[0]) 
                    month = int(input_date.split('.')[1])
                    year = int(input_date.split('.')[2])
                    your_date = datetime(year, month, day)
                    break
                except Exception as e:
                    print('You entered the wrong date')
                   
            
            my_salon.add_nail_polish_to_list(input_color, input_type, your_date) 
         
            print('-----------------------------------------')
            print('Nail polish added')
            print('-----------------------------------------')


        if preferred_operation == to_scv:
            clear = lambda: os.system('cls')
            clear()

            my_salon.save_nail_polish_mas_ser_to_df_to_csv()
            print('-----------------------------------------')
            print('The file is written')
            print('-----------------------------------------')



        if preferred_operation == from_scv:
            clear = lambda: os.system('cls')
            clear()

            my_salon.to_list_nail_polish_mas_from_csv()
            print('-----------------------------------------')
            print('The file is written')
            print('-----------------------------------------')



        if preferred_operation == show_masters:
            clear = lambda: os.system('cls')
            clear()
            
            print('-----------------------------------------')
            my_salon.print_all_mas()
            print('-----------------------------------------')



        if preferred_operation == show_services:
            clear = lambda: os.system('cls')
            clear()
            
            print('-----------------------------------------')
            my_salon.print_all_ser()
            print('-----------------------------------------')



        if preferred_operation == show_nail_polish:
            clear = lambda: os.system('cls')
            clear()
            
            print('-----------------------------------------')
            my_salon.print_all_nail_polish()
            print('-----------------------------------------')     



        if preferred_operation == exit:        

            clear = lambda: os.system('cls')
            clear()
            print('-----------------------------------------') 
            print('See you soon') 
            print('-----------------------------------------')  
            break


start_program()


