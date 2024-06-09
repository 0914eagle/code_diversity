
def get_max_fruits(n, v, a, b):
    # Sort the fruits by their ripening day in ascending order
    sorted_fruits = sorted(zip(a, b), key=lambda x: x[0])

    # Initialize the variables
    total_fruits = 0
    current_day = 1
    collected_fruits = 0

    # Iterate through the fruits and collect them on the appropriate days
    for fruit in sorted_fruits:
        ripening_day, num_fruits = fruit
        while current_day <= ripening_day:
            collected_fruits += min(v - collected_fruits, num_fruits)
            total_fruits += collected_fruits
            current_day += 1
            collected_fruits = 0

    return total_fruits

