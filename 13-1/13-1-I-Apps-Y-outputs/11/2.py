
def get_max_days(a, b, c):
    # Initialize variables
    max_days = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Iterate over each day of the week
    for day in days:
        # Check if the current day is a day when the cat eats fish food
        if day in ["Monday", "Thursday", "Sunday"]:
            # If the current day is a day when the cat eats fish food, check if there are enough fish food rations in the backpack
            if a >= 1:
                # If there are enough fish food rations in the backpack, increment the maximum number of days the cat can eat in a trip without additional food purchases
                max_days += 1
                # Decrement the number of fish food rations in the backpack
                a -= 1
        # Check if the current day is a day when the cat eats rabbit stew
        elif day in ["Tuesday", "Saturday"]:
            # If the current day is a day when the cat eats rabbit stew, check if there are enough rabbit stew rations in the backpack
            if b >= 1:
                # If there are enough rabbit stew rations in the backpack, increment the maximum number of days the cat can eat in a trip without additional food purchases
                max_days += 1
                # Decrement the number of rabbit stew rations in the backpack
                b -= 1
        # Check if the current day is a day when the cat eats chicken stake
        else:
            # If the current day is a day when the cat eats chicken stake, check if there are enough chicken stake rations in the backpack
            if c >= 1:
                # If there are enough chicken stake rations in the backpack, increment the maximum number of days the cat can eat in a trip without additional food purchases
                max_days += 1
                # Decrement the number of chicken stake rations in the backpack
                c -= 1
    
    # Return the maximum number of days the cat can eat in a trip without additional food purchases
    return max_days

