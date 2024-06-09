
def get_valid_ids(n, pattern):
    # Initialize a list to store the valid IDs
    valid_ids = []
    
    # Iterate through all possible binary strings of length n
    for i in range(2**n):
        # Convert the current integer to a binary string
        binary_string = bin(i)[2:]
        # Pad the string with leading 0s to make it length n
        binary_string = binary_string.zfill(n)
        # Check if the string satisfies the pattern
        if satisfies_pattern(binary_string, pattern):
            # If it does, add it to the list of valid IDs
            valid_ids.append(binary_string)
    
    # Return the list of valid IDs
    return valid_ids

def satisfies_pattern(string, pattern):
    # Check if the string and pattern have the same length
    if len(string) != len(pattern):
        return False
    
    # Initialize a counter to keep track of the number of 1s in the string
    num_ones = 0
    
    # Iterate through the characters of the string and pattern simultaneously
    for i in range(len(string)):
        # Check if the current character of the string is a 1
        if string[i] == "1":
            # Increment the counter
            num_ones += 1
        # Check if the current character of the pattern is a *
        if pattern[i] == "*":
            # Return True, since the string can satisfy the pattern
            return True
    
    # Check if the number of 1s in the string is at least half the length of the string
    if num_ones >= len(string) // 2:
        # Return True, since the string can satisfy the pattern
        return True
    
    # Otherwise, return False
    return False

def get_maximum_number_of_members(n, pattern):
    # Get the list of valid IDs
    valid_ids = get_valid_ids(n, pattern)
    # Return the number of valid IDs
    return len(valid_ids)

if __name__ == '__main__':
    # Read the input from stdin
    n = int(input())
    pattern = input()
    
    # Call the function to get the maximum number of members
    maximum_number_of_members = get_maximum_number_of_members(n, pattern)
    
    # Print the result
    print(maximum_number_of_members)

