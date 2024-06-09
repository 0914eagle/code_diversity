
def get_maximum_total_income(sequence, k):
    # Sort the sequence in non-decreasing order
    sequence.sort()
    
    # Initialize the total income and the number of changes made
    total_income = sum(sequence)
    changes_made = 0
    
    # Loop through the sequence and change the sign of each number
    for i in range(len(sequence)):
        # Check if the number of changes made is less than the given number of changes
        if changes_made < k:
            # Change the sign of the current number
            sequence[i] *= -1
            # Increment the total income and the number of changes made
            total_income += sequence[i]
            changes_made += 1
    
    # Return the maximum total income
    return total_income

def main():
    # Read the input sequence and the number of changes from stdin
    n, k = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    # Call the get_maximum_total_income function and print the result
    print(get_maximum_total_income(sequence, k))

if __name__ == '__main__':
    main()

