
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
            shelves.append(i)
            max_bottles = max(max_bottles, len(shelves))
        else:
            # Add a new shelf and place the bottle on it
            current_height = bottle
            shelves.append(i)
            max_bottles = max(max_bottles, len(shelves))

    return max_bottles

