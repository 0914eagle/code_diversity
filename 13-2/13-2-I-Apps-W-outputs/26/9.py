
def get_max_bottles(bottles, fridge_height):
    # Initialize variables
    max_bottles = 0
    current_height = 0
    shelves = []

    # Iterate through the bottles
    for bottle in bottles:
        # Check if the current height plus the height of the current bottle is less than or equal to the fridge height
        if current_height + bottle <= fridge_height:
            # Add the height of the current bottle to the current height
            current_height += bottle
            # Increment the number of bottles that can be placed
            max_bottles += 1
        else:
            # If the current height plus the height of the current bottle is greater than the fridge height,
            # add a shelf and reset the current height
            shelves.append(current_height)
            current_height = bottle

    # Add the last shelf
    shelves.append(current_height)

    # Return the maximum number of bottles that can be placed and the shelves
    return max_bottles, shelves

def main():
    # Read the input
    n, h = map(int, input().split())
    bottles = list(map(int, input().split()))

    # Get the maximum number of bottles that can be placed and the shelves
    max_bottles, shelves = get_max_bottles(bottles, h)

    # Print the maximum number of bottles that can be placed
    print(max_bottles)

if __name__ == '__main__':
    main()

