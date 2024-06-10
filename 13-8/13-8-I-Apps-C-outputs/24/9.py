
def get_max_value(sequence):
    # Find the maximum value in the sequence
    max_value = max(sequence)
    
    # Initialize a list to store the indices of the maximum value
    max_indices = [i for i, x in enumerate(sequence) if x == max_value]
    
    # If the maximum value is at the end of the sequence, return it
    if max_indices[-1] == len(sequence) - 1:
        return max_value, 0
    
    # If the maximum value is not at the end of the sequence, find the next maximum value
    next_max_value = max(sequence[max_indices[-1] + 1:])
    next_max_indices = [i + max_indices[-1] + 1 for i, x in enumerate(sequence[max_indices[-1] + 1:]) if x == next_max_value]
    
    # If the next maximum value is at the end of the sequence, return the current maximum value
    if next_max_indices[-1] == len(sequence) - 1:
        return max_value, 0
    
    # If the next maximum value is not at the end of the sequence, find the next maximum value after that
    after_next_max_value = max(sequence[next_max_indices[-1] + 1:])
    after_next_max_indices = [i + next_max_indices[-1] + 1 for i, x in enumerate(sequence[next_max_indices[-1] + 1:]) if x == after_next_max_value]
    
    # If the after next maximum value is at the end of the sequence, return the current maximum value
    if after_next_max_indices[-1] == len(sequence) - 1:
        return max_value, 0
    
    # If the after next maximum value is not at the end of the sequence, find the next maximum value after that
    final_max_value = max(sequence[after_next_max_indices[-1] + 1:])
    final_max_indices = [i + after_next_max_indices[-1] + 1 for i, x in enumerate(sequence[after_next_max_indices[-1] + 1:]) if x == final_max_value]
    
    # Return the final maximum value and the number of operations performed
    return final_max_value, len(final_max_indices)

def main():
    # Read the input sequence from stdin
    sequence = list(map(int, input().split()))
    
    # Find the maximum value and the number of operations performed
    max_value, num_operations = get_max_value(sequence)
    
    # Print the maximum value and the number of operations
    print(max_value)
    print(num_operations)
    
    # Print the indices of the elements chosen in each operation
    for i in range(num_operations):
        print(i + 1)

if __name__ == '__main__':
    main()

