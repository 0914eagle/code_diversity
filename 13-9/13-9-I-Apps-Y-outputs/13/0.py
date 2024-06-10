
def is_good_sequence(sequence):
    # Check if the sequence is empty
    if not sequence:
        return True
    
    # Check if the sequence has only one element
    if len(sequence) == 1:
        return False
    
    # Check if the sequence has at least two elements
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if sequence[i] + sequence[j] == 2**k for k in range(32):
                return True
    
    # If the sequence has more than two elements and no combination of two elements sums to a power of two, return False
    return False

def get_minimum_elements_to_remove(sequence):
    # Initialize a variable to keep track of the minimum number of elements to remove
    min_elements_to_remove = len(sequence)
    
    # Iterate over the range of possible number of elements to remove
    for num_elements_to_remove in range(1, len(sequence)+1):
        # Get the subset of the sequence with the first num_elements_to_remove elements removed
        subset = sequence[num_elements_to_remove:]
        
        # Check if the subset is good
        if is_good_sequence(subset):
            # If the subset is good, update the minimum number of elements to remove
            min_elements_to_remove = min(min_elements_to_remove, num_elements_to_remove)
    
    # Return the minimum number of elements to remove
    return min_elements_to_remove

def main():
    # Read the input sequence from stdin
    n = int(input())
    sequence = list(map(int, input().split()))
    
    # Get the minimum number of elements to remove to make the sequence good
    min_elements_to_remove = get_minimum_elements_to_remove(sequence)
    
    # Print the minimum number of elements to remove
    print(min_elements_to_remove)

if __name__ == '__main__':
    main()

