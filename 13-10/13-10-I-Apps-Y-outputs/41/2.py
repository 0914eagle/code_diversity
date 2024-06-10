
def get_max_days(a, b, c):
    # Initialize the maximum number of days as 0
    max_days = 0
    # Iterate over the days of the week
    for day in range(1, 8):
        # Calculate the number of days the cat can eat in a trip without additional food purchases
        num_days = get_num_days(day, a, b, c)
        # Update the maximum number of days if necessary
        if num_days > max_days:
            max_days = num_days
    # Return the maximum number of days
    return max_days

def get_num_days(day, a, b, c):
    # Initialize the number of days as 0
    num_days = 0
    # Iterate over the days of the week
    for i in range(1, 8):
        # Calculate the number of portions of food the cat can eat on the current day
        num_portions = get_num_portions(day, i, a, b, c)
        # Update the number of days if the cat can eat at least one portion of food on the current day
        if num_portions > 0:
            num_days += 1
    # Return the number of days
    return num_days

def get_num_portions(day, current_day, a, b, c):
    # Initialize the number of portions as 0
    num_portions = 0
    # Check if the cat can eat fish food on the current day
    if day in [1, 3, 5, 7] and current_day in [1, 3, 5, 7]:
        num_portions += a
    # Check if the cat can eat rabbit stew on the current day
    elif day in [2, 4, 6] and current_day in [2, 4, 6]:
        num_portions += b
    # Check if the cat can eat chicken stakes on the current day
    else:
        num_portions += c
    # Return the number of portions
    return num_portions

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(get_max_days(a, b, c))

