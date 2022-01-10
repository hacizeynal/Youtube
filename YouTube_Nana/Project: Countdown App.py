import datetime

user_input_goal = input("Please enter your goal and deadline separated with comma:\n")
user_input_list = user_input_goal.split(":")

goal = user_input_list [ 0 ]
deadline = user_input_list [ 1 ]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
# calculation how many days from now till deadline

calculate_how_many_days_left = deadline_date - today_date

print(f"Dear user ! Time remaining for your {goal} is {calculate_how_many_days_left.days} days")
