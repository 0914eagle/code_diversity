
def get_longest_magical_permutation(n, s):
    # Sort the input set in ascending order
    s = sorted(s)
    
    # Initialize the longest magical permutation length as 0
    longest_magical_permutation_length = 0
    
    # Initialize the magical permutation as an empty list
    magical_permutation = []
    
    # Iterate over all possible lengths of the magical permutation
    for length in range(1, n):
        # Initialize the current magical permutation as an empty list
        current_magical_permutation = []
        
        # Iterate over all possible starting indices for the magical permutation
        for start_index in range(0, n - length + 1):
            # Check if the current magical permutation is valid
            if is_magical_permutation(current_magical_permutation, s):
                # If the current magical permutation is valid, update the longest magical permutation length and the magical permutation
                longest_magical_permutation_length = length
                magical_permutation = current_magical_permutation
                break
            # Add the next element to the current magical permutation
            current_magical_permutation.append(s[start_index + length - 1])
    
    # Return the longest magical permutation length and the magical permutation
    return longest_magical_permutation_length, magical_permutation

def is_magical_permutation(permutation, s):
    # Check if the permutation is valid
    for i in range(len(permutation) - 1):
        # Check if the bitwise xor of any two consecutive elements in the permutation is an element in the set S
        if permutation[i] ^ permutation[i + 1] not in s:
            return False
    
    # If all consecutive elements in the permutation have a bitwise xor that is an element in the set S, the permutation is valid
    return True

n = int(input())
s = list(map(int, input().split()))

# Call the function to get the longest magical permutation length and the magical permutation
longest_magical_permutation_length, magical_permutation = get_longest_magical_permutation(n, s)

# Print the longest magical permutation length
print(longest_magical_permutation_length)

# Print the magical permutation
print(*magical_permutation)

