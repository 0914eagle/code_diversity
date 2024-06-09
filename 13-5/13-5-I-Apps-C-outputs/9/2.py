
import itertools

def get_valid_ids(n, pattern):
    
    # Initialize an empty list to store the valid IDs
    valid_ids = []
    
    # Iterate over all possible binary strings of length n
    for binary_string in itertools.product([0, 1], repeat=n):
        # Check if the current binary string satisfies the pattern
        if satisfies_pattern(binary_string, pattern):
            # If it does, add it to the list of valid IDs
            valid_ids.append("".join(map(str, binary_string)))
    
    return valid_ids

def satisfies_pattern(binary_string, pattern):
    
    # If the binary string and the pattern have different lengths, return False
    if len(binary_string) != len(pattern):
        return False
    
    # Initialize a counter to keep track of the number of 1s in the binary string
    count = 0
    
    # Iterate over the binary string and the pattern simultaneously
    for b, p in zip(binary_string, pattern):
        # If the current element of the binary string is 1 and the current element of the pattern is *, increment the counter
        if b == 1 and p == "*":
            count += 1
    
    # If the counter is greater than or equal to half the length of the binary string, return True
    return count >= len(binary_string) // 2

def get_max_spies(n, pattern):
    
    # Get all valid IDs of length n that satisfy the pattern
    valid_ids = get_valid_ids(n, pattern)
    
    # Return the number of valid IDs
    return len(valid_ids)

if __name__ == '__main__':
    n = int(input())
    pattern = input()
    print(get_max_spies(n, pattern))

