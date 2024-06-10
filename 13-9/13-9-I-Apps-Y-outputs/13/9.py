
def is_good_sequence(sequence):
    # Check if the sequence is empty
    if not sequence:
        return True
    
    # Check if any two elements in the sequence add up to a power of two
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if is_power_of_two(sequence[i] + sequence[j]):
                return True
    
    # If we reach this point, the sequence is not good
    return False

def is_power_of_two(n):
    return n > 0 and not (n & (n - 1))

def get_min_elements_to_remove(sequence):
    # Check if the sequence is already good
    if is_good_sequence(sequence):
        return 0
    
    # Initialize the minimum number of elements to remove to the length of the sequence
    min_elements_to_remove = len(sequence)
    
    # Iterate over all possible subsets of the sequence
    for i in range(1, len(sequence) + 1):
        # Check if the subset is good
        if is_good_sequence(sequence[:i]):
            # If it is good, calculate the number of elements to remove
            elements_to_remove = len(sequence) - i
            # Update the minimum number of elements to remove if necessary
            if elements_to_remove < min_elements_to_remove:
                min_elements_to_remove = elements_to_remove
    
    # Return the minimum number of elements to remove
    return min_elements_to_remove

def main():
    sequence_length = int(input())
    sequence = list(map(int, input().split()))
    print(get_min_elements_to_remove(sequence))

if __name__ == '__main__':
    main()

