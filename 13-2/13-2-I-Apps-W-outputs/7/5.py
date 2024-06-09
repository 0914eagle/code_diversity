
def is_odd_sequence(sequence):
    # Check if the length of the sequence is odd
    if len(sequence) % 2 == 1:
        # Initialize a flag to keep track of whether the requirements are met
        requirements_met = True
        # Iterate through the sequence and check if each subsegment meets the requirements
        for i in range(1, len(sequence), 2):
            # Check if the subsegment is odd in length
            if len(sequence[i:i+2]) % 2 == 1:
                # Check if the first and last elements of the subsegment are odd
                if sequence[i] % 2 == 1 and sequence[i+1] % 2 == 1:
                    continue
            # If any of the subsegments do not meet the requirements, set the flag to False
            requirements_met = False
            break
        # Return True if all subsegments meet the requirements, False otherwise
        return requirements_met
    # If the length of the sequence is even, return False
    else:
        return False

def main():
    # Test the is_odd_sequence function with different inputs
    sequence1 = [1, 3, 5]
    sequence2 = [1, 0, 1, 5, 1]
    sequence3 = [4, 3, 1]
    sequence4 = [3, 9, 9, 3]
    print(is_odd_sequence(sequence1)) # Should print "Yes"
    print(is_odd_sequence(sequence2)) # Should print "Yes"
    print(is_odd_sequence(sequence3)) # Should print "No"
    print(is_odd_sequence(sequence4)) # Should print "No"

if __name__ == '__main__':
    main()

