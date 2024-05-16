


def intTry(value):
    try:
        your_num = int(value)
        return True
    except ValueError:
        return False
    



def what_to_do(first_num, second_num):
    whats_the_operration = input('What operation should be performed from +, -, *, / ?: ')

    division = '/'
    multiplication = '*'
    addition = '+'
    subtraction = '-'



    possible_var = (division, multiplication, addition, subtraction)
    while whats_the_operration not in possible_var:
        whats_the_operration = input('What operation should be performed from +, -, *, / ?: ')

    if whats_the_operration == division:
        result = int(first_num) / int(second_num)
        print(int(result))

    if whats_the_operration == multiplication:
        result = int(first_num) * int(second_num)
        print(result)

    if whats_the_operration == addition:
        result = int(first_num) + int(second_num)
        print(result)

    if whats_the_operration == subtraction:
        result = int(first_num) - int(second_num)
        print(result)   

    return result





def enter_your_num(num_val):
    val = input('Enter ' + num_val + ' number: ')

    is_it_int_first = intTry(val)
    while is_it_int_first == False:
        val = input('Enter ' + num_val + ' number: ') 
        is_it_int_first = intTry(val)

    return val




def to_be_continue():
    is_it_continue = input('Would you like to continue? Answer yes or no: ')

    yes_or_no = ('yes', 'no')
    while is_it_continue not in yes_or_no:
        is_it_continue = input('Would you like to continue? Answer yes or no: ')




#start
def my_calculator():
    first_num = enter_your_num('first')
    second_num = enter_your_num('second')
    result = what_to_do(first_num, second_num)

    what_about_continue = to_be_continue()

    while what_about_continue == 'yes':
        use_res = input('Would you like to use the previous result?: ') 

        yes_or_no = ('yes', 'no')
        while use_res not in yes_or_no:
            use_res = input('Would you like to use the previous result?: ') 

        if use_res == 'yes':
            first_num = int(result)
            second_num = enter_your_num('second')
            result = what_to_do(first_num, second_num)

        else:
            first_num = enter_your_num('first')
            second_num = enter_your_num('second')
            result = what_to_do(first_num, second_num)

        what_about_continue = to_be_continue()



my_calculator()
