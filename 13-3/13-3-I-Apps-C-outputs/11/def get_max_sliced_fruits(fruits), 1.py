
def get_max_sliced_fruits(fruits):
    # Sort the fruits by their x-coordinates
    sorted_fruits = sorted(fruits, key=lambda x: x[0])

    # Initialize the maximum number of sliced fruits
    max_sliced_fruits = 0

    # Iterate over the fruits
    for i in range(len(sorted_fruits)):
        # Get the current fruit
        fruit = sorted_fruits[i]

        # Initialize the number of sliced fruits for this fruit
        sliced_fruits = 0

        # Iterate over the remaining fruits
        for j in range(i+1, len(sorted_fruits)):
            # Get the next fruit
            next_fruit = sorted_fruits[j]

            # Check if the line segment between the current and next fruit intersects with the inner part or the boundary of the current fruit
            if intersects_with_fruit(fruit, next_fruit):
                # Increment the number of sliced fruits for this fruit
                sliced_fruits += 1

        # Update the maximum number of sliced fruits
        max_sliced_fruits = max(max_sliced_fruits, sliced_fruits)

    return max_sliced_fruits

def intersects_with_fruit(fruit, next_fruit):
    # Get the x-coordinates of the line segment
    x1, y1 = fruit
    x2, y2 = next_fruit

    # Check if the line segment intersects with the inner part or the boundary of the fruit
    return (x1 <= x2 and x2 <= x1 + 2*math.pi) or (x1 >= x2 and x2 >= x1 - 2*math.pi)

