
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
            subsegments[-1].append(sequence[i])
        else:
            # If an even number is found, start a new subsegment
            subsegments.append([sequence[i]])
    # Return the list of subsegments
    return subsegments

def main():
    # Read the input sequence from stdin
    sequence = list(map(int, input().split()))
    # Check if the sequence can be divided into an odd number of subsegments
    if is_odd_sequence(sequence):
        # If it can, divide it into subsegments and print the result
        subsegments = divide_sequence(sequence)
        print(subsegments)
    else:
        # If it can't, print "No"
        print("No")

if __name__ == '__main__':
    main()

