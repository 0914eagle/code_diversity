
def get_max_fruits(n, v, a, b):
    # Sort the fruits by their ripening day in ascending order
    sorted_fruits = sorted(zip(a, b), key=lambda x: x[0])

    # Initialize the variables
    max_fruits = 0
    current_day = 1
    collected_fruits = 0

    # Iterate through the fruits and collect them on the appropriate days
    for fruit in sorted_fruits:
        # If the current day is the day the fruit ripens, collect all the fruits from that tree
        if current_day == fruit[0]:
            max_fruits += fruit[1]
            collected_fruits += fruit[1]
        # If the current day is the day after the fruit ripens, collect only the remaining fruits from that tree
        elif current_day == fruit[0] + 1:
            max_fruits += fruit[1] - collected_fruits
            collected_fruits = 0
        # If the current day is later than the day the fruit ripens, skip the fruit
        else:
            continue

        # Increment the current day
        current_day += 1

        # If the number of collected fruits is equal to the limit, break the loop
        if collected_fruits == v:
            break

    return max_fruits

