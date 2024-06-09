
def get_max_fruits_sliced(fruits):
    # Sort the fruits by their x-coordinate
    sorted_fruits = sorted(fruits, key=lambda x: x[0])

    # Initialize the maximum number of fruits sliced
    max_fruits_sliced = 0

    # Iterate over the fruits
    for i in range(len(sorted_fruits)):
        # Get the current fruit
        current_fruit = sorted_fruits[i]

        # Initialize the number of fruits sliced with this fruit
        fruits_sliced = 1

        # Iterate over the remaining fruits
        for j in range(i+1, len(sorted_fruits)):
            # Get the next fruit
            next_fruit = sorted_fruits[j]

            # Check if the next fruit is within the slice of the current fruit
            if next_fruit[0] <= current_fruit[0] + current_fruit[1]:
                # Increment the number of fruits sliced with this fruit
                fruits_sliced += 1

        # Update the maximum number of fruits sliced
        max_fruits_sliced = max(max_fruits_sliced, fruits_sliced)

    return max_fruits_sliced

