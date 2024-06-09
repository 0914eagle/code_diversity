
def get_max_bottles(bottle_heights, fridge_height):
    
    # Initialize variables
    max_bottles = 0
    current_height = 0
    bottles_placed = 0

    # Iterate through the bottles
    for bottle_height in bottle_heights:
        # Check if the current bottle fits on the current shelf
        if current_height + bottle_height <= fridge_height:
            # If it fits, place the bottle on the current shelf and update the current height
            current_height += bottle_height
            bottles_placed += 1
        else:
            # If it doesn't fit, start a new shelf
            current_height = bottle_height
            bottles_placed = 1

        # Update the maximum number of bottles placed
        max_bottles = max(max_bottles, bottles_placed)

    return max_bottles

