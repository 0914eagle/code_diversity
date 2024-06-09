
def get_valid_ids(n, pattern):
    # Initialize a list to store the valid IDs
    valid_ids = []
    
    # Iterate through all possible binary strings of length n
    for i in range(2**n):
        # Convert the integer to a binary string
        binary_string = bin(i)[2:]
        # Pad the string with zeros if it is less than n digits long
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
    
    # Initialize a counter for the number of 1s in the string
    num_ones = 0
    
    # Iterate through the characters of the string and pattern simultaneously
    for c1, c2 in zip(string, pattern):
        # If the current character of the string is 1 and the current character of the pattern is 1, increment the counter
        if c1 == "1" and c2 == "1":
            num_ones += 1
    
    # If the counter is greater than or equal to half the length of the string, return True
    if num_ones >= len(string) // 2:
        return True
    else:
        return False

def get_max_spies(n, pattern):
    # Get the list of valid IDs
    valid_ids = get_valid_ids(n, pattern)
    # Return the number of valid IDs
    return len(valid_ids)

if __name__ == '__main__':
    n = int(input())
    pattern = input()
    print(get_max_spies(n, pattern))

