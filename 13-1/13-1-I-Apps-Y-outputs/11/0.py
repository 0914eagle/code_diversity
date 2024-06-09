
def get_max_days(a, b, c):
    # Initialize the maximum number of days to 0
    max_days = 0
    
    # Iterate over all possible days of the week
    for day in range(1, 8):
        # Calculate the number of days the cat can eat in a trip without additional food purchases for the current day
        num_days = get_num_days(day, a, b, c)
        
        # Update the maximum number of days if the current day has the maximum number of days
        if num_days > max_days:
            max_days = num_days
    
    # Return the maximum number of days
    return max_days

def get_num_days(day, a, b, c):
    # Initialize the number of days to 0
    num_days = 0
    
    # Iterate over all possible days of the week
    for i in range(1, 8):
        # Calculate the current day of the week
        current_day = (day + i - 1) % 7 + 1
        
        # Check if the current day is a day when the cat eats fish food
        if current_day in [1, 4, 7]:
            # Decrement the number of fish food rations by 1
            a -= 1
        
        # Check if the current day is a day when the cat eats rabbit stew
        elif current_day in [2, 6]:
            # Decrement the number of rabbit stew rations by 1
            b -= 1
        
        # Check if the current day is a day when the cat eats chicken stake
        else:
            # Decrement the number of chicken stake rations by 1
            c -= 1
        
        # Increment the number of days by 1
        num_days += 1
        
        # Check if all food rations have been used
        if a <= 0 and b <= 0 and c <= 0:
            # Break the loop
            break
    
    # Return the number of days
    return num_days

# Test the function with example inputs
assert get_max_days(2, 1, 1) == 4
assert get_max_days(3, 2, 2) == 7
assert get_max_days(1, 100, 1) == 3
assert get_max_days(30, 20, 10) == 39

