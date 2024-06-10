
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
            if sequence[i] + sequence[j] == 2**k for k in range(32):
                return True
    
    # If the sequence does not have two elements or more, it is not good
    return False

def get_min_elements_to_remove(sequence):
    # Initialize a variable to store the minimum number of elements to remove
    min_elements_to_remove = len(sequence)
    
    # Iterate over the range of possible numbers of elements to remove
    for num_elements_to_remove in range(len(sequence)):
        # Check if removing the current number of elements will make the sequence good
        if is_good_sequence(sequence[:-num_elements_to_remove]):
            # If it will, update the minimum number of elements to remove
            min_elements_to_remove = min(min_elements_to_remove, num_elements_to_remove)
    
    # Return the minimum number of elements to remove
    return min_elements_to_remove

def main():
    # Read the length of the sequence and the sequence of integers
    n = int(input())
    sequence = [int(x) for x in input().split()]
    
    # Call the function to get the minimum number of elements to remove and print the result
    print(get_min_elements_to_remove(sequence))

if __name__ == '__main__':
    main()

