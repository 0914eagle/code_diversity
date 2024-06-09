
def get_day_of_week(day, month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Calculate the number of days since January 1st, 2009
    days_since_jan1 = days_in_month[month-1] + day
    for i in range(1, month-1):
        days_since_jan1 += days_in_month[i]
    
    # Calculate the day of the week
    day_of_week = (days_since_jan1 + 6) % 7
    
    return days_in_week[day_of_week]

