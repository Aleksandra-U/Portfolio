
**The project counting the days of life lived**

Description: the user enters the date of birth, and the program counts the number of days between the date of his birth and the current day


Methods: 
1.your_birthday – the main method

2.check_future – the method checks if the user entered a date from the future 

3.getting_date - checking the correctness of date numbers

4.intTry – checks for a number




**The calculator project**
Description: calculator

Methods: 
1.my_calculator – the main method
2.to_be_continue – the method asks if the user wants to continue 
3.enter_your_num – the method requests a number from the user
4.what_to_do – request the operation
5.intTry – checks for a number




**The car dealership project**
There are two classes in the project: Car, Car_Dealership
   
Class Car_Dealership
Fields: list_car, profit 
Methods: 
1.	add_car_to_dealership: add an instance of the class Car to list_car
2.	save_list_car_to_df_to_csv: saving the list_car list to a Dataframe and then to a CSV-file
3.	take_list_car_from_scv: read the CSV-file, write it to the Dataframe and write it to the list_car
4.	print_all_car: output to the console list_car
5.	to_sell_car: remove an object from list_car and add its value to the field profit 
6.	print_all_profit: output the data of the profit field to the console
   
Class Car 
Fields: color, mark, price
A custom menu has also been implemented where the user can work with the Car_Dealership class and added an input check




**The beauty salon project**
There are three classes in the project: Services, Masters, Nail_polish, Salon

Class Salon
Fields: list_masters, list_nail_polish
Methods: 
1.	add_mas_to_list: add an instance of the Masters class to the list_mas
2.	add_nail_polish_to_list: add an instance of the class Nail_polish in list_nail_polish
7.	save_nail_polish_mas_ser_to_df_to_csv: saving list_nail_polish and list_mas in Dataframe and after to в CSV-file
8.	to_list_nail_polish_mas_from_csv:  read CSV-file, write them to the Dataframe and write them to list_masters and list_nail_polish
3.	print_all_mas: output the list_mas field data to the consol
4.	print_all_ser: output the type_servisces field data from list_mas to the consol 
5.	print_all_nail_polish: output the list_nail_polish field data to the consol 

Class Services
Fields: type, price, how_long

Class Masters
Fields: name, age, gender, type_servisces

Class Nail_polish
Fields: color, type, expiration_date

A custom menu has also been implemented where the user can work with the specified classes and added an input check. 


