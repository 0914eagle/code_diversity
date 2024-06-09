
def is_odd_sequence(sequence):
    # Check if the length of the sequence is odd
    if len(sequence) % 2 == 1:
        # Initialize a flag to keep track of whether the requirements are met
        requirements_met = True
        # Iterate through the sequence and check if each subsegment has an odd length and begins and ends with an odd number
        for i in range(1, len(sequence), 2):
            # Check if the subsegment has an odd length
            if len(sequence[i:i+2]) % 2 == 1:
                # Check if the first and last elements of the subsegment are odd
                if sequence[i] % 2 == 1 and sequence[i+1] % 2 == 1:
                    continue
                else:
                    requirements_met = False
                    break
            else:
                requirements_met = False
                break
        return "Yes" if requirements_met else "No"
    else:
        return "No"

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    print(is_odd_sequence(sequence))

if __name__ == '__main__':
    main()

