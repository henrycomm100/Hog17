from datetime import datetime, timedelta

def get_next_weekday(current_date, weekday):
    days_until_target_day = (weekday - current_date.weekday() + 7) % 7
    next_weekday_date = current_date + timedelta(days=days_until_target_day)
    return next_weekday_date

# Get the current date
current_date = datetime.now()

# Define the target weekday (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
target_weekday = 0  # Monday

# Get the date of the next Monday
next_weekday_date = get_next_weekday(current_date, target_weekday)

print("Current date:", current_date.strftime('%Y-%m-%d'))
print("Next Monday:", next_weekday_date.strftime('%Y-%m-%d'))


def get_next_monday():
    # Get the current date
    current_date = datetime.now()
    days_until_next_monday = (7 - current_date.weekday()) % 7
    next_weekday_date = current_date + timedelta(days=days_until_next_monday)
    
    print("Next Monday:", next_weekday_date.strftime('%Y-%m-%d'))
    return next_weekday_date.strftime('%Y-%m-%d')

get_next_monday()

date_dict = { 
              "$first_day$":
                [
                  "09:00 AM",
                  "09:30 AM",
                ],
}

date_dict[get_next_monday()]= date_dict.pop("$first_day$")
print(date_dict)