
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

def solve(sequence):
    # Check if the sequence is an odd sequence
    if is_odd_sequence(sequence):
        # If it is, return "Yes"
        return "Yes"
    else:
        # If it's not, return "No"
        return "No"

if __name__ == '__main__':
    sequence = [int(i) for i in input().split()]
    print(solve(sequence))

