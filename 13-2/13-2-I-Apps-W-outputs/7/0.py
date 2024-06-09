
def is_odd_sequence(sequence):
    # Check if the length of the sequence is odd
    if len(sequence) % 2 == 1:
        # Initialize a flag to keep track of whether the requirements are met
        requirements_met = True
        # Iterate through the sequence and check if each subsegment is valid
        for i in range(1, len(sequence), 2):
            # Check if the subsegment is valid
            if sequence[i] % 2 == 0 or sequence[i-1] % 2 == 0:
                # If the subsegment is not valid, set the flag to False
                requirements_met = False
                break
        # Return True if the requirements are met, False otherwise
        return requirements_met
    # If the length of the sequence is even, return False
    else:
        return False

def main():
    # Read the input sequence from stdin
    sequence = list(map(int, input().split()))
    # Call the is_odd_sequence function and print the result
    print("Yes" if is_odd_sequence(sequence) else "No")

if __name__ == '__main__':
    main()

