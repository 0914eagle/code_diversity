
def get_max_bottles(bottles, fridge_height):
    # Initialize variables
    max_bottles = 0
    current_bottles = 0
    current_height = 0

    # Iterate through the bottles
    for bottle in bottles:
        # Check if the current bottle fits on the current shelf
        if current_height + bottle <= fridge_height:
            # If it fits, add it to the current shelf and update the current height
            current_bottles += 1
            current_height += bottle
        else:
            # If it doesn't fit, start a new shelf
            max_bottles = max(max_bottles, current_bottles)
            current_bottles = 1
            current_height = bottle

    # Add the last shelf
    max_bottles = max(max_bottles, current_bottles)

    return max_bottles

