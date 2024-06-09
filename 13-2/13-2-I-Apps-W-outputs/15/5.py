
def get_max_bottles(bottles, fridge_height):
    # Initialize variables
    max_bottles = 0
    current_bottles = 0
    current_height = 0

    # Iterate through the bottles
    for bottle in bottles:
        # Check if the current bottle fits on the current shelf
        if current_height + bottle <= fridge_height:
            # Add the current bottle to the current shelf
            current_bottles += 1
            current_height += bottle
        else:
            # Check if the current shelf is the largest one so far
            if current_bottles > max_bottles:
                max_bottles = current_bottles

            # Start a new shelf
            current_bottles = 1
            current_height = bottle

    # Check if the last shelf is the largest one so far
    if current_bottles > max_bottles:
        max_bottles = current_bottles

    return max_bottles

