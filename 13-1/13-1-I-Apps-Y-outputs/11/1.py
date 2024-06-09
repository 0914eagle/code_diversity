
def get_max_days(a, b, c):
    # Initialize variables
    max_days = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Iterate over each day of the week
    for day in days:
        # Calculate the number of days the cat can eat in a trip without additional food purchases
        if day == "Monday" or day == "Thursday" or day == "Sunday":
            num_days = a
        elif day == "Tuesday" or day == "Saturday":
            num_days = b
        else:
            num_days = c
        max_days = max(max_days, num_days)
    
    return max_days

