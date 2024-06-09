
def is_good_sequence(sequence):
    # Check if the sequence is strictly increasing
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return False
    
    # Check if any two adjacent elements are coprime
    for i in range(len(sequence) - 1):
        if gcd(sequence[i], sequence[i + 1]) == 1:
            return False
    
    return True

def longest_good_sequence(good_integers):
    # Initialize the longest good sequence as an empty list
    longest_sequence = []
    
    # Iterate over the good integers
    for i in range(len(good_integers)):
        # Check if the current integer is a good integer
        if good_integers[i] in longest_sequence:
            continue
        
        # Initialize the current sequence as a list with the current integer
        current_sequence = [good_integers[i]]
        
        # Iterate over the remaining good integers
        for j in range(i + 1, len(good_integers)):
            # Check if the current integer is a good integer and is adjacent to the last element of the current sequence
            if good_integers[j] in longest_sequence and good_integers[j] == current_sequence[-1] + 1:
                # Add the current integer to the current sequence
                current_sequence.append(good_integers[j])
            
            # Check if the current sequence is a good sequence
            if is_good_sequence(current_sequence):
                # Check if the current sequence is longer than the longest sequence found so far
                if len(current_sequence) > len(longest_sequence):
                    # Update the longest sequence found so far
                    longest_sequence = current_sequence
            
            # Break if the current sequence is not a good sequence
            else:
                break
    
    # Return the length of the longest sequence found
    return len(longest_sequence)

def main():
    # Read the number of good integers and the list of good integers from stdin
    n = int(input())
    good_integers = [int(x) for x in input().split()]
    
    # Find the length of the longest good sequence
    longest_sequence_length = longest_good_sequence(good_integers)
    
    # Print the length of the longest good sequence
    print(longest_sequence_length)

if __name__ == '__main__':
    main()

