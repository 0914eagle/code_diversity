
def get_k_incremental_double_free_string(k, n):
    import itertools
    
    # Initialize a list to store the generated strings
    strings = []
    
    # Iterate over all possible strings of length k
    for letters in itertools.product(range(26), repeat=k):
        # Check if the string is k-incremental and double free
        if is_k_incremental_double_free(letters, k):
            # Add the string to the list
            strings.append("".join(chr(ord('a') + letter) for letter in letters))
    
    # Return the nth string in the list, or -1 if it doesn't exist
    try:
        return strings[n-1]
    except IndexError:
        return -1

# Check if a string is k-incremental and double free
def is_k_incremental_double_free(string, k):
    # Check if the string is k-incremental
    if not is_k_incremental(string, k):
        return False
    
    # Check if the string is double free
    if not is_double_free(string):
        return False
    
    return True

# Check if a string is k-incremental
def is_k_incremental(string, k):
    # Initialize a dictionary to store the number of occurrences of each letter
    occurrences = {}
    
    # Iterate over the letters in the string
    for letter in string:
        # If the letter is not already in the dictionary, add it with a count of 1
        if letter not in occurrences:
            occurrences[letter] = 1
        # Otherwise, increment the count of the letter
        else:
            occurrences[letter] += 1
    
    # Check if the string is k-incremental
    for i in range(1, k+1):
        # If the number of occurrences of the ith letter is not equal to i, the string is not k-incremental
        if occurrences.get(i-1, 0) != i:
            return False
    
    return True

# Check if a string is double free
def is_double_free(string):
    # Iterate over the letters in the string
    for i in range(len(string)-1):
        # If the ith and i+1th letters are the same, the string is not double free
        if string[i] == string[i+1]:
            return False
    
    return True

# Test the function
print(get_k_incremental_double_free_string(2, 650)) # Should print "zyz"
print(get_k_incremental_double_free_string(2, 651)) # Should print "-1"

