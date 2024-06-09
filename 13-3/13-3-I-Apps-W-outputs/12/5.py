
def get_max_fruits(n, v, a, b):
    # Sort the fruits by their ripening day in ascending order
    sorted_fruits = sorted(zip(a, b), key=lambda x: x[0])

    # Initialize the variables
    total_fruits = 0
    current_day = 1
    fruits_collected = 0

    # Loop through the fruits and collect them on the appropriate days
    for fruit in sorted_fruits:
        ripening_day, num_fruits = fruit

        # If the current day is equal to the ripening day, collect all the fruits
        if current_day == ripening_day:
            total_fruits += num_fruits
            fruits_collected += num_fruits

        # If the current day is one day after the ripening day, collect as many fruits as possible
        elif current_day == ripening_day + 1:
            total_fruits += min(v - fruits_collected, num_fruits)
            fruits_collected = 0

        # Increment the current day
        current_day += 1

    return total_fruits

