
def get_max_value(sequence):
    # Initialize variables
    max_value = 0
    max_sequence = []
    n = len(sequence)
    
    # Base case: if the sequence has only one element, return it
    if n == 1:
        return sequence[0]
    
    # Recursive case: find the maximum value and the sequence that leads to it
    for i in range(n):
        # If the element is at either end of the sequence, delete it
        if i == 0 or i == n-1:
            seq = sequence[:i] + sequence[i+1:]
        # If the element is not at either end of the sequence, replace it with the sum of the two elements that are adjacent to it and delete them
        else:
            seq = sequence[:i] + [sequence[i] + sequence[i+1]] + sequence[i+2:]
        # Recursively call the function with the updated sequence
        value = get_max_value(seq)
        # If the value is greater than the current maximum value, update the maximum value and the corresponding sequence
        if value > max_value:
            max_value = value
            max_sequence = seq
    
    # Return the maximum value and the sequence that leads to it
    return max_value, max_sequence

def print_sequence(sequence):
    # Print the number of operations
    print(len(sequence))
    # Print the sequence of chosen elements
    for i in range(len(sequence)):
        print(sequence[i]+1)

if __name__ == '__main__':
    # Read the input
    n = int(input())
    sequence = list(map(int, input().split()))
    # Call the function to get the maximum value and the sequence that leads to it
    max_value, max_sequence = get_max_value(sequence)
    # Print the maximum value
    print(max_value)
    # Call the function to print the sequence of chosen elements
    print_sequence(max_sequence)

