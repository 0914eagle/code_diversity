
def get_smallest_k(doors):
    # Initialize variables
    k = 0
    left_doors = 0
    right_doors = 0

    # Iterate through the doors
    for door in doors:
        # If the door is located in the left exit, increment the left doors counter
        if door == 0:
            left_doors += 1
        # If the door is located in the right exit, increment the right doors counter
        else:
            right_doors += 1

        # If either the left or right doors counter is equal to the number of doors, return the current value of k
        if left_doors == len(doors) or right_doors == len(doors):
            return k

        # Increment k
        k += 1

    # If the function reaches this point, it means that the house was not able to be exited, so return -1
    return -1

def main():
    # Read the number of doors
    n = int(input())

    # Read the sequence of doors
    doors = list(map(int, input().split()))

    # Call the get_smallest_k function and print the result
    print(get_smallest_k(doors))

if __name__ == '__main__':
    main()

