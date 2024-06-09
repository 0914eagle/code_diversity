
def get_max_bottles(bottles, height):
    # Initialize a list to store the maximum number of bottles that can be placed on each shelf
    max_bottles = [0] * height
    # Initialize a variable to store the maximum number of bottles that can be placed in the fridge
    max_total_bottles = 0
    # Loop through the bottles
    for bottle in bottles:
        # Loop through the shelves
        for i in range(height):
            # Check if the bottle fits on the current shelf
            if bottle <= height - i:
                # Update the maximum number of bottles that can be placed on the current shelf
                max_bottles[i] += 1
                # Update the maximum number of bottles that can be placed in the fridge
                max_total_bottles = max(max_total_bottles, max_bottles[i])
                # Break out of the loop since we have found a valid placement for the bottle
                break
    # Return the maximum number of bottles that can be placed in the fridge
    return max_total_bottles

def main():
    # Read the number of bottles and the height of the fridge from stdin
    n, h = map(int, input().split())
    # Read the heights of the bottles from stdin
    bottles = list(map(int, input().split()))
    # Call the get_max_bottles function and print the result
    print(get_max_bottles(bottles, h))

if __name__ == '__main__':
    main()

