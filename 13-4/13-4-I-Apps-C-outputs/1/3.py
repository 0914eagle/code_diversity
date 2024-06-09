
def solve(k, n):
    # Initialize a list to store the results
    results = []
    
    # Iterate through all possible strings of length k
    for i in range(26**k):
        # Convert the current index to a string
        string = chr(i + 97)
        
        # Check if the string is double free
        if is_double_free(string):
            # Check if the string is k-incremental
            if is_k_incremental(string, k):
                # Add the string to the results list
                results.append(string)
    
    # Return the nth string in the results list, or -1 if it doesn't exist
    try:
        return results[n-1]
    except IndexError:
        return -1

# Check if a string is double free
def is_double_free(string):
    # Check if any two adjacent characters are the same
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return False
    return True

# Check if a string is k-incremental
def is_k_incremental(string, k):
    # Initialize a dictionary to store the frequency of each character
    freq = {}
    
    # Iterate through each character in the string
    for char in string:
        # If the character is not already in the dictionary, add it with a frequency of 1
        if char not in freq:
            freq[char] = 1
        # Otherwise, increment the frequency of the character
        else:
            freq[char] += 1
    
    # Check if the string has the correct length
    if len(string) != sum(range(1, k+1)):
        return False
    
    # Check if the string has exactly one character with each frequency
    for i in range(1, k+1):
        if i not in freq.values():
            return False
    
    return True

