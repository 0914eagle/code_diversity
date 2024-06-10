
def get_smallest_k(n, sequence):
    # Initialize variables
    k = 0
    left_doors = 0
    right_doors = 0

    # Iterate through the sequence
    for i in range(n):
        # Check if the current door is in the left or right exit
        if sequence[i] == 0:
            left_doors += 1
        else:
            right_doors += 1

        # If both exits have at least one open door, return the current index
        if left_doors > 0 and right_doors > 0:
            return k

        # Increment the index
        k += 1

    # If the end of the sequence is reached and both exits still don't have at least one open door, return -1
    return -1

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    print(get_smallest_k(n, sequence))

if __name__ == '__main__':
    main()

