
def get_max_bottles(bottle_heights, fridge_height):
    # Initialize variables
    max_bottles = 0
    current_height = 0
    bottles_on_shelf = 0

    # Iterate through the bottles
    for bottle_height in bottle_heights:
        # Check if the current bottle fits on the current shelf
        if current_height + bottle_height <= fridge_height:
            # If it fits, add it to the current shelf and update the current height
            current_height += bottle_height
            bottles_on_shelf += 1
        else:
            # If it doesn't fit, move to the next shelf
            max_bottles = max(max_bottles, bottles_on_shelf)
            current_height = bottle_height
            bottles_on_shelf = 1

    # Add the last shelf
    max_bottles = max(max_bottles, bottles_on_shelf)

    return max_bottles

