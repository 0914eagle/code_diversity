
def get_max_fruits(fruits):
    # Sort the fruits by their x-coordinate
    sorted_fruits = sorted(fruits, key=lambda x: x[0])

    # Initialize the maximum number of fruits that can be sliced
    max_fruits = 0

    # Iterate over the fruits
    for i in range(len(sorted_fruits)):
        # Get the current fruit
        fruit = sorted_fruits[i]

        # Check if the fruit is within the range of the previous fruit
        if i > 0 and fruit[0] - sorted_fruits[i - 1][0] <= 2:
            # If the fruit is within the range, increment the maximum number of fruits
            max_fruits += 1

        # Check if the fruit is within the range of the next fruit
        if i < len(sorted_fruits) - 1 and sorted_fruits[i + 1][0] - fruit[0] <= 2:
            # If the fruit is within the range, increment the maximum number of fruits
            max_fruits += 1

    return max_fruits

