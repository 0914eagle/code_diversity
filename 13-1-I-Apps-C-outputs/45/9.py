
def get_max_fruits(fruits):
    # Sort the fruits by their x-coordinate
    sorted_fruits = sorted(fruits, key=lambda x: x[0])

    # Initialize the maximum number of fruits that can be sliced
    max_fruits = 0

    # Iterate over the fruits
    for i in range(len(sorted_fruits)):
        # Get the current fruit
        fruit = sorted_fruits[i]

        # Check if the fruit is within the range of the previous fruits
        for j in range(i):
            # Get the previous fruit
            previous_fruit = sorted_fruits[j]

            # Check if the current fruit is within the range of the previous fruit
            if fruit[0] >= previous_fruit[0] and fruit[0] <= previous_fruit[1]:
                # Increment the maximum number of fruits that can be sliced
                max_fruits += 1
                break

    return max_fruits

