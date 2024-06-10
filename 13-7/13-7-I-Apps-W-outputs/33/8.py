
def get_exit_door(doors):
    # Initialize variables
    left_doors = 0
    right_doors = 0
    exit_door = 0

    # Iterate through the list of doors
    for door in doors:
        # If the current door is located in the left exit, increment the left doors counter
        if door == 0:
            left_doors += 1
        # If the current door is located in the right exit, increment the right doors counter
        else:
            right_doors += 1

        # If the current door is located in the left exit and the right doors counter is greater than zero, set the exit door to the current door
        if door == 0 and right_doors > 0:
            exit_door = door
            break

    # Return the exit door
    return exit_door

def get_smallest_k(doors):
    # Initialize variables
    k = 0
    left_doors = 0
    right_doors = 0

    # Iterate through the list of doors
    for door in doors:
        # If the current door is located in the left exit, increment the left doors counter
        if door == 0:
            left_doors += 1
        # If the current door is located in the right exit, increment the right doors counter
        else:
            right_doors += 1

        # If the current door is located in the left exit and the right doors counter is greater than zero, set the exit door to the current door
        if door == 0 and right_doors > 0:
            k = len(doors) - left_doors
            break

    # Return the smallest k
    return k

def main():
    # Read the number of doors and the sequence of doors from the input
    n = int(input())
    doors = list(map(int, input().split()))

    # Get the exit door
    exit_door = get_exit_door(doors)

    # Get the smallest k
    k = get_smallest_k(doors)

    # Print the result
    print(k)

if __name__ == '__main__':
    main()

