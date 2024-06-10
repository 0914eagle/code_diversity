
def get_max_value(sequence):
    # Initialize variables
    max_value = 0
    operations = 0
    selection = []

    # Loop through the sequence
    for i in range(len(sequence)):
        # Check if the element is at either end of the sequence
        if i == 0 or i == len(sequence) - 1:
            # Delete the element
            sequence.pop(i)
            operations += 1
        else:
            # Replace the element with the sum of the two adjacent elements
            sequence[i] = sequence[i - 1] + sequence[i + 1]
            # Delete the two adjacent elements
            sequence.pop(i - 1)
            sequence.pop(i - 1)
            operations += 2

        # Update the maximum value
        max_value = max(max_value, sequence[0])

    # Return the maximum value and the number of operations
    return max_value, operations, selection

def main():
    # Read the input
    N = int(input())
    sequence = list(map(int, input().split()))

    # Get the maximum value and the number of operations
    max_value, operations, selection = get_max_value(sequence)

    # Print the output
    print(max_value)
    print(operations)
    for i in selection:
        print(i)

if __name__ == '__main__':
    main()

