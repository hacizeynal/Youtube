calculation_to_units = 1.7
name_of_unit = "manat"


def dollar_to_manat(dollar):
    return f'{dollar} $ equals {dollar * calculation_to_units} {name_of_unit}'

def validate_and_execute():
    try:
        user_input_number = float(user_input)
#       user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = dollar_to_manat(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0 ,please enter positive number")
        else:
            print("Please enter positive number")

    except ValueError:
        print('Please enter positive valid number')

user_input = input('Zehmet olmasa mueyyen etdiyiniz meblegi qeyd edin:\n')
validate_and_execute()

