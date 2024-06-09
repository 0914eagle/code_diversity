
def get_max_days(a, b, c):
    # Initialize variables
    max_days = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Iterate over each day of the week
    for day in days:
        # Check if the current day is a day with fish food
        if day in ["Monday", "Thursday", "Sunday"]:
            # If the current day is a day with fish food, check if there are enough fish food in the backpack
            if a >= 1:
                # If there are enough fish food in the backpack, increment the maximum number of days
                max_days += 1
                # Decrement the number of fish food in the backpack
                a -= 1
            else:
                # If there are not enough fish food in the backpack, break the loop
                break
        # Check if the current day is a day with rabbit stew
        elif day in ["Tuesday", "Saturday"]:
            # If the current day is a day with rabbit stew, check if there are enough rabbit stew in the backpack
            if b >= 1:
                # If there are enough rabbit stew in the backpack, increment the maximum number of days
                max_days += 1
                # Decrement the number of rabbit stew in the backpack
                b -= 1
            else:
                # If there are not enough rabbit stew in the backpack, break the loop
                break
        # Check if the current day is a day with chicken stake
        else:
            # If the current day is a day with chicken stake, check if there are enough chicken stake in the backpack
            if c >= 1:
                # If there are enough chicken stake in the backpack, increment the maximum number of days
                max_days += 1
                # Decrement the number of chicken stake in the backpack
                c -= 1
            else:
                # If there are not enough chicken stake in the backpack, break the loop
                break
    
    # Return the maximum number of days
    return max_days

