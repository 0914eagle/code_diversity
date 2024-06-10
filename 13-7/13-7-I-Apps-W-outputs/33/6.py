
def get_smallest_index(doors):
    # Initialize variables
    left_doors = 0
    right_doors = 0
    index = 0

    # Iterate through the doors
    for door in doors:
        # If the door is located in the left exit, increment the left doors counter
        if door == 0:
            left_doors += 1
        # If the door is located in the right exit, increment the right doors counter
        else:
            right_doors += 1

        # If both exits have at least one open door, return the current index
        if left_doors > 0 and right_doors > 0:
            return index

        # Increment the index
        index += 1

    # If the function reaches this point, it means that Mr. Black was not able to exit the house
    return -1

def main():
    # Read the number of doors
    n = int(input())

    # Read the sequence of doors
    doors = list(map(int, input().split()))

    # Call the function to get the smallest index
    result = get_smallest_index(doors)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

