
def get_smallest_k(n, sequence):
    # Initialize variables
    k = 0
    left_exit = 0
    right_exit = 0

    # Iterate through the sequence
    for i in range(n):
        # Check if the current door is in the left or right exit
        if sequence[i] == 0:
            left_exit += 1
        else:
            right_exit += 1

        # If both exits have at least one open door, return the current index
        if left_exit > 0 and right_exit > 0:
            return k

        # Increment the index
        k += 1

    # If the function reaches this point, it means that Mr. Black was not able to exit the house
    return -1

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    print(get_smallest_k(n, sequence))

if __name__ == '__main__':
    main()

