
def fruit_slicer(fruits):
    # Initialize a list to store the sliced fruits
    sliced_fruits = []

    # Iterate over the fruits
    for fruit in fruits:
        # Check if the fruit has already been sliced
        if fruit not in sliced_fruits:
            # Slice the fruit and add it to the list of sliced fruits
            sliced_fruits.append(fruit)

    # Return the number of sliced fruits
    return len(sliced_fruits)

