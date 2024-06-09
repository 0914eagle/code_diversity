
def get_maximum_income(sequence, k):
    # Sort the sequence in non-decreasing order
    sequence.sort()
    
    # Initialize the total income and the number of swaps made
    total_income = sum(sequence)
    num_swaps = 0
    
    # Loop through the sequence and find the pairs of numbers with opposite signs
    for i in range(len(sequence) - 1):
        if sequence[i] * sequence[i + 1] < 0:
            # If the signs are opposite, flip the sign of the second number and increment the number of swaps made
            sequence[i + 1] *= -1
            num_swaps += 1
    
    # If the number of swaps made is less than the given number of swaps, flip the sign of the first number
    if num_swaps < k:
        sequence[0] *= -1
        num_swaps += 1
    
    # Return the maximum total income after the swaps
    return sum(sequence)

def main():
    # Read the input sequence and the number of swaps from stdin
    n, k = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    # Call the get_maximum_income function and print the result
    print(get_maximum_income(sequence, k))

if __name__ == '__main__':
    main()

