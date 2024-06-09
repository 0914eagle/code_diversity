
def get_k_incremental_double_free_string(k, n):
    # Initialize a list to store the characters that will be used in the string
    chars = []
    # Initialize a variable to keep track of the length of the string
    length = 0
    # Initialize a variable to keep track of the number of strings generated
    count = 0
    # Iterate through the alphabet
    for char in range(97, 123):
        # Convert the current character to a string
        char = chr(char)
        # If the length of the string plus the length of the current character is less than or equal to k, append the current character to the string
        if length + len(char) <= k:
            chars.append(char)
            length += len(char)
        # If the length of the string is equal to k, generate all possible combinations of the characters in the string
        if length == k:
            for combination in itertools.permutations(chars):
                # If the combination is double free and has the correct length, increment the count and check if it is the nth string
                if is_double_free(combination) and len(combination) == k:
                    count += 1
                    if count == n:
                        return "".join(combination)
        # If the length of the string is greater than k, return -1
        if length > k:
            return -1
    # If no string is found, return -1
    return -1

# Check if a string is double free
def is_double_free(string):
    # Iterate through the characters in the string
    for i in range(len(string) - 1):
        # If the current character is the same as the next character, return False
        if string[i] == string[i + 1]:
            return False
    # If no adjacent characters are the same, return True
    return True

