
def get_valid_ids(n, pattern):
    # Initialize a list to store the valid IDs
    valid_ids = []
    
    # Iterate through all possible binary strings of length n
    for i in range(2**n):
        # Convert the current binary string to a list of digits
        binary_string = list(str(bin(i)[2:]))
        
        # Check if the current binary string satisfies the pattern
        if satisfies_pattern(binary_string, pattern):
            # If it does, add it to the list of valid IDs
            valid_ids.append("".join(binary_string))
    
    # Return the list of valid IDs
    return valid_ids

def satisfies_pattern(binary_string, pattern):
    # If the length of the binary string is not equal to the length of the pattern, return False
    if len(binary_string) != len(pattern):
        return False
    
    # Initialize a counter to keep track of the number of 1s in the binary string
    count = 0
    
    # Iterate through the binary string and pattern simultaneously
    for i in range(len(binary_string)):
        # If the current character in the binary string is 1 and the current character in the pattern is *, increment the counter
        if binary_string[i] == "1" and pattern[i] == "*":
            count += 1
    
    # If the counter is greater than or equal to half the length of the binary string, return True
    if count >= len(binary_string) // 2:
        return True
    
    # Otherwise, return False
    return False

def get_max_members(n, pattern):
    # Get the list of valid IDs
    valid_ids = get_valid_ids(n, pattern)
    
    # Return the maximum number of members that can be assigned unique IDs
    return 2**n - len(valid_ids)

if __name__ == '__main__':
    n = int(input())
    pattern = input()
    print(get_max_members(n, pattern))

