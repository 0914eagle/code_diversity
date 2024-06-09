
def is_odd_sequence(sequence):
    # Check if the length of the sequence is odd
    if len(sequence) % 2 == 1:
        # Initialize a flag to keep track of whether the requirements are met
        requirements_met = True
        # Iterate through the sequence and check if each element is odd
        for i in range(len(sequence)):
            if sequence[i] % 2 == 0:
                # If an even number is found, set the flag to False
                requirements_met = False
                break
        # Return True if the requirements are met, False otherwise
        return requirements_met
    else:
        # If the length of the sequence is even, return False
        return False

def divide_sequence(sequence):
    # Initialize a list to store the subsegments
    subsegments = []
    # Iterate through the sequence and check if each element is odd
    for i in range(len(sequence)):
        if sequence[i] % 2 == 1:
            # If an odd number is found, add it to the current subsegment
            subsegments.append(sequence[i])
        else:
            # If an even number is found, start a new subsegment
            subsegments.append([sequence[i]])
    # Return the list of subsegments
    return subsegments

def main():
    # Test the functions with example inputs
    sequence1 = [1, 3, 5]
    sequence2 = [1, 0, 1, 5, 1]
    sequence3 = [4, 3, 1]
    sequence4 = [3, 9, 9, 3]
    print(is_odd_sequence(sequence1)) # Should print "Yes"
    print(is_odd_sequence(sequence2)) # Should print "Yes"
    print(is_odd_sequence(sequence3)) # Should print "No"
    print(is_odd_sequence(sequence4)) # Should print "No"
    print(divide_sequence(sequence1)) # Should print [[1, 3, 5]]
    print(divide_sequence(sequence2)) # Should print [[1, 0, 1], [5], [1]]
    print(divide_sequence(sequence3)) # Should print [[4], [3, 1]]
    print(divide_sequence(sequence4)) # Should print [[3, 9, 9], [3]]

if __name__ == '__main__':
    main()

