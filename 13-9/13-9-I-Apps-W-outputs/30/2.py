
def get_valid_rearrangements(A, B):
    # Initialize variables
    n = len(A)
    valid_rearrangements = 0
    
    # Iterate through all possible groups of students
    for i in range(n):
        for j in range(i+1, n+1):
            # Check if the group of students is valid
            if is_valid_group(A, i, j):
                # Increment the number of valid rearrangements
                valid_rearrangements += 1
    
    # Return the number of valid rearrangements
    return valid_rearrangements

def is_valid_group(A, i, j):
    # Initialize variables
    n = len(A)
    group = A[i:j]
    
    # Check if the group is valid
    if len(group) == 0:
        return False
    if i == 0 and j == n:
        return True
    if i > 0 and j < n:
        return True
    return False

def main():
    # Read the input
    A = input()
    B = input()
    
    # Call the get_valid_rearrangements function
    valid_rearrangements = get_valid_rearrangements(A, B)
    
    # Print the output
    print(valid_rearrangements)

if __name__ == '__main__':
    main()

