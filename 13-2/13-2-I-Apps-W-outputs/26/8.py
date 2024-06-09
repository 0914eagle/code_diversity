
def get_max_bottles(bottle_heights, fridge_height):
    
    # Initialize variables
    max_bottles = 0
    current_height = 0
    bottles_placed = 0

    # Iterate through the bottles
    for bottle_height in bottle_heights:
        # Check if the current bottle fits on the current shelf
        if current_height + bottle_height <= fridge_height:
            # If it fits, update the current height and number of bottles placed
            current_height += bottle_height
            bottles_placed += 1
        else:
            # If it doesn't fit, update the maximum number of bottles and reset the current height
            max_bottles = max(max_bottles, bottles_placed)
            current_height = bottle_height
            bottles_placed = 1

    # Return the maximum number of bottles placed
    return max(max_bottles, bottles_placed)

