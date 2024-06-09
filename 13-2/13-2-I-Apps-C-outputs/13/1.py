
def get_max_fruits(fruits):
    # Sort the fruits by their x-coordinate
    sorted_fruits = sorted(fruits, key=lambda x: x[0])

    # Initialize the maximum number of fruits that can be sliced
    max_fruits = 0

    # Iterate over the fruits
    for i in range(len(sorted_fruits)):
        # Get the current fruit
        fruit = sorted_fruits[i]

        # Check if the fruit is already sliced
        if fruit[1] <= 0:
            continue

        # Initialize the number of fruits that can be sliced with this fruit
        num_fruits = 1

        # Iterate over the remaining fruits
        for j in range(i+1, len(sorted_fruits)):
            # Get the next fruit
            next_fruit = sorted_fruits[j]

            # Check if the next fruit is already sliced
            if next_fruit[1] <= 0:
                break

            # Check if the next fruit is within the slice of the current fruit
            if next_fruit[0] >= fruit[0] and next_fruit[1] >= fruit[1]:
                num_fruits += 1
                next_fruit[1] = 0

        # Update the maximum number of fruits if necessary
        max_fruits = max(max_fruits, num_fruits)

    return max_fruits

