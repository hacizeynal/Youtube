user_input_message = 'Dear user ,please enter number of days and conversion unit!:\n'

def days_and_units(num_of_days,conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24*60} minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24*60*60} seconds"
    else:
        return "Unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_and_units(user_input_number,days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0 ,please enter positive number")
        else:
            print("Please enter positive number")
    except ValueError:
        print('Please enter positive valid number ,do not ruin program')

