
def get_smallest_index(sequence):
    # Initialize variables
    left_exit = 0
    right_exit = 0
    k = 0

    # Iterate through the sequence
    for i in range(len(sequence)):
        # If the current door is located in the left exit, increment the left exit counter
        if sequence[i] == 0:
            left_exit += 1
        # If the current door is located in the right exit, increment the right exit counter
        else:
            right_exit += 1

        # If both exits have at least one open door, return the current index
        if left_exit > 0 and right_exit > 0:
            return k

        # Increment the index
        k += 1

    # If we reach this point, it means that Mr. Black was not able to exit the house
    return -1

def main():
    # Read the number of doors and the sequence of opened doors
    n = int(input())
    sequence = list(map(int, input().split()))

    # Find the smallest index such that Mr. Black can exit the house
    k = get_smallest_index(sequence)

    # Print the result
    print(k)

if __name__ == '__main__':
    main()

