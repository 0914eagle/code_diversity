
def get_max_bottles(bottles, fridge_height):
    # Initialize variables
    max_bottles = 0
    current_height = 0
    shelves = []

    # Iterate through the bottles
    for bottle in bottles:
        # Check if the current height plus the height of the bottle is less than or equal to the fridge height
        if current_height + bottle <= fridge_height:
            # Add the height of the bottle to the current height
            current_height += bottle
            # Increment the number of bottles that can be placed
            max_bottles += 1
        else:
            # If the current height plus the height of the bottle is greater than the fridge height,
            # check if the bottle can be placed on a shelf
            if len(shelves) > 0 and shelves[-1] + bottle <= fridge_height:
                # Add the height of the bottle to the last shelf
                shelves[-1] += bottle
                # Increment the number of bottles that can be placed
                max_bottles += 1
            else:
                # If the bottle cannot be placed on a shelf, break the loop
                break

    # Return the maximum number of bottles that can be placed
    return max_bottles

def main():
    # Read the input
    n, h = map(int, input().split())
    bottles = list(map(int, input().split()))

    # Call the function to get the maximum number of bottles that can be placed
    max_bottles = get_max_bottles(bottles, h)

    # Print the result
    print(max_bottles)

if __name__ == '__main__':
    main()

