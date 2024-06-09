
def get_max_bottles(bottles, fridge_height):
    # Initialize variables
    max_bottles = 0
    current_height = 0
    shelves = []

    # Iterate through the bottles
    for i, bottle in enumerate(bottles):
        # Check if the current bottle fits on the current shelf
        if current_height + bottle <= fridge_height:
            # Add the bottle to the current shelf
            current_height += bottle
            shelves.append(bottle)
            max_bottles = i + 1
        else:
            # Check if the current bottle fits on a new shelf
            if len(shelves) < fridge_height - 1:
                # Add a new shelf and add the bottle to it
                shelves.append(bottle)
                current_height = bottle
                max_bottles = i + 1
            else:
                # The bottle does not fit in the fridge
                break

    return max_bottles

