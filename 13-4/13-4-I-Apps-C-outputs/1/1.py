
def solve(k, n):
    # Initialize a list to store the results
    results = []
    
    # Iterate through all possible strings
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
    return results[n-1] if n <= len(results) else -1

# Check if a string is double free
def is_double_free(string):
    # Iterate through the string
    for i in range(len(string) - 1):
        # Check if the current character is the same as the next character
        if string[i] == string[i+1]:
            # If it is, return False
            return False
    
    # If we reach this point, the string is double free
    return True

# Check if a string is k-incremental
def is_k_incremental(string, k):
    # Initialize a dictionary to store the frequency of each character
    freq = {}
    
    # Iterate through the string
    for c in string:
        # If the character is not already in the dictionary, add it with a frequency of 1
        if c not in freq:
            freq[c] = 1
        # If the character is already in the dictionary, increment its frequency
        else:
            freq[c] += 1
    
    # Check if the frequency of each character is k-incremental
    for c, f in freq.items():
        # If the frequency is not k-incremental, return False
        if f != k:
            return False
    
    # If we reach this point, the string is k-incremental
    return True

