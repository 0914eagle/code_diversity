
def is_good_sequence(sequence):
    # Check if the sequence is empty
    if not sequence:
        return True
    
    # Check if the sequence has only one element
    if len(sequence) == 1:
        return False
    
    # Check if the sequence has two or more elements
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if is_power_of_two(sequence[i] + sequence[j]):
                return True
    
    # If the sequence has two or more elements and no pair of elements sums to a power of two, then it is not good
    return False

def is_power_of_two(n):
    return (n != 0) and (n & (n-1) == 0)

def get_minimum_elements_to_remove(sequence):
    # Check if the sequence is already good
    if is_good_sequence(sequence):
        return 0
    
    # Initialize variables
    minimum_elements_to_remove = len(sequence)
    current_sequence = sequence.copy()
    
    # Iterate through the elements of the sequence
    for i in range(len(sequence)):
        # Remove the current element from the sequence and check if the resulting sequence is good
        current_sequence.pop(i)
        if is_good_sequence(current_sequence):
            # If the resulting sequence is good, update the minimum number of elements to remove
            minimum_elements_to_remove = min(minimum_elements_to_remove, len(sequence) - len(current_sequence))
        
        # Add the current element back to the sequence
        current_sequence.insert(i, sequence[i])
    
    # Return the minimum number of elements to remove
    return minimum_elements_to_remove

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    print(get_minimum_elements_to_remove(sequence))

