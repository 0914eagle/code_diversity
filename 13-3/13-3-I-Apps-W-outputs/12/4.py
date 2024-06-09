
def get_max_fruits(n, v, a, b):
    # Sort the fruits by their ripening day in ascending order
    sorted_fruits = sorted(zip(a, b), key=lambda x: x[0])

    # Initialize the variables
    total_fruits = 0
    current_day = 1
    collected_fruits = 0

    # Loop through the fruits and collect them on the appropriate days
    for fruit in sorted_fruits:
        # If the current day is less than or equal to the ripening day of the fruit, collect it
        if current_day <= fruit[0]:
            total_fruits += fruit[1]
            collected_fruits += 1

        # If the number of collected fruits is equal to v, move to the next day
        if collected_fruits == v:
            current_day += 1
            collected_fruits = 0

    return total_fruits

