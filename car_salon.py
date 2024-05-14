



import os
import pandas as pd


class Car:
    def __init__(self, car_color, car_mark, car_price):
        self.color = car_color 
        self.mark = car_mark
        self.price = car_price
      
class car_dealership:
    def __init__(self, car_list, all_profit):
        self.list_car = car_list 
        self.profit = all_profit

    def add_car_to_dealership (self, color_car, mark_car, car_price):
        car1 = Car(color_car, mark_car, car_price) 
        
        self.list_car.append(car1)


    def save_list_car_to_df_to_csv(self):
        df = []
        for my_car in self.list_car:
            under_df = (my_car.color, my_car.mark, my_car.price) 
            df.append(under_df)
        my_df = pd.DataFrame(df,columns=['color', 'mark', 'price'])    
        my_df.to_csv('my_car.csv', index=False)


    def take_list_car_from_scv(self):
        df = pd.read_csv('my_car.csv')
        print(df)
        for index, row in df.iterrows(): 
            self.list_car.append(Car(row.color, row.mark, row.price))
 

    def print_all_car(self):
        print('Cars are available at the dealership: ')
        for every_car in self.list_car:
            print(f'Color: {every_car.color}, Mark: {every_car.mark}, Price: ${every_car.price}')

    def to_sell_car(self, index):
        all_possible_i = []
        for i in range(0, len(self.list_car)):
            all_possible_i.append(i+1)

        if index in all_possible_i:
            car_to_del = self.list_car[index-1]
            price_car_to_del = car_to_del.price
            self.profit += price_car_to_del
            print(f'machine color {car_to_del.color}, mark {car_to_del.mark} bought at a price ${car_to_del.price}')
            del self.list_car [index-1]
        else:
            print('There is no car under this index.\n'
                  'Please, look at the available options.\n'
                   'To do this, press 3 when asked "What operation do you want to perform" ')             

    def print_all_profit(self):
        print(f'The entire profit of the car dealership = {self.profit}')










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


def which_operration():
    whats_the_operation = input('What kind of operation would you like to perform?\n'
                                '1. Add a car to the dealership \n'
                                '2. Write to the CSV-file \n'
                                '3. Upload from CSV-file \n'
                                '4. See available options \n'
                                '3. Sell the car \n'
                                '5. View the profit received \n'
                                '6. Exit the menu \n'
                                'Please, choose the number 1, 2, 3, 4, 5 or 6 to continue: ' )
    return whats_the_operation




def try_int(value):
    try:
        your_num = int(value)
        return True
    except Exception as e:
        print('You didnt enter a number')
        return False






def start_program():
    dealer1 = car_dealership([], 0) 

    dealer1.add_car('blue', 'Mazda', 1000)
    dealer1.add_car('green', 'Lada', 2000)
    dealer1.add_car('yellow', 'Lexus', 245)

    while True:
        preferred_operation = which_operration()

        check_int_num = try_int_which_num(preferred_operation)
        while check_int_num == False:
            preferred_operation = which_operration()
            check_int_num = try_int_which_num(preferred_operation)

        add_car = '1'
        to_scv = '2'
        from_scv = '3'
        watch_variant = '4'
        sell = '5'
        how_much_profit = '5'
        exit_menu = '6'
        

        if preferred_operation == add_car:
            clear = lambda: os.system('cls')
            clear()

            your_color = input('What color a car do you want to add?: ')
            your_mark = input('What brend of a car do you want to add?: ')

            your_cost = input('What is the price of this car?: ')

            check_int = try_int(your_cost)
            while check_int == False:
                your_cost = input('What is the price of this car?: ')
                check_int = try_int(your_cost)


            dealer1.add_car_to_dealership(your_color, your_mark, your_cost)

            print('-----------------------------------------')
            print('The car has been added')
            print('-----------------------------------------')





        if preferred_operation == to_scv:
            clear = lambda: os.system('cls')
            clear()
            
            dealer1.save_list_car_to_df_to_csv()
            print('-----------------------------------------')
            print('The file is written')
            print('-----------------------------------------')


        
        if preferred_operation == from_scv:
            clear = lambda: os.system('cls')
            clear()

            dealer1.take_list_car_from_scv()
            print('-----------------------------------------')
            print('The file is written')
            print('-----------------------------------------')


        
        if preferred_operation == watch_variant:

            clear = lambda: os.system('cls')
            clear()
            print('-----------------------------------------')
            dealer1.print_all_car()        
            print('-----------------------------------------')




        if preferred_operation == sell:

            clear = lambda: os.system('cls')
            clear()

            to_sell = input('Which car number do you want to sell?: ')

            check_int = try_int(your_cost)
            while check_int == False:
                to_sell = input('Which car number do you want to sell?: ')
                check_int = try_int(your_cost)



            car_num = to_sell
            dealer1.to_sell_car(int(car_num))

            print('-----------------------------------------')
            print('The car is sold')
            print('-----------------------------------------')


        

        if preferred_operation == how_much_profit:

            clear = lambda: os.system('cls')
            clear()

            print('-----------------------------------------')
            dealer1.print_all_profit()
            print('-----------------------------------------')



        if preferred_operation == exit_menu:

            clear = lambda: os.system('cls')
            clear()

            print('-----------------------------------------')
            print('See you soon')  
            print('-----------------------------------------')
            break
            
    
start_program()     