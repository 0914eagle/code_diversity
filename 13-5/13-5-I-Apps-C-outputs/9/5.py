
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
    # Check if the string is the same length as the pattern
    if len(string) != len(pattern):
        return False
    
    # Initialize a counter for the number of 1s in the string
    num_ones = 0
    
    # Iterate through the characters of the string and pattern simultaneously
    for i in range(len(string)):
        # If the character in the string is 1 and the character in the pattern is not *, increment the counter
        if string[i] == "1" and pattern[i] != "*":
            num_ones += 1
        # If the character in the string is * and the character in the pattern is not 1, return False
        elif string[i] == "*" and pattern[i] == "1":
            return False
    
    # If the counter is greater than or equal to half the length of the string, return True
    return num_ones >= len(string) // 2

def get_max_members(n, pattern):
    # Get the list of valid IDs
    valid_ids = get_valid_ids(n, pattern)
    # Return the number of valid IDs
    return len(valid_ids)

if __name__ == '__main__':
    # Read the input
    n = int(input())
    pattern = input()
    # Call the function to get the maximum number of members
    max_members = get_max_members(n, pattern)
    # Print the result
    print(max_members)

