
def get_k_incremental_double_free_string(k, n):
    # Initialize a list to store the generated strings
    strings = []
    
    # Iterate over all possible strings of length k
    for i in range(26**k):
        # Convert the integer i to a string of length k
        string = chr(i % 26 + ord('a')) * k
        
        # Check if the string is double free
        if all(string[i] != string[i+1] for i in range(len(string)-1)):
            # Check if the string is k-incremental
            counts = [string.count(c) for c in string]
            if all(counts[i] == i for i in range(1, k+1)):
                # If both conditions are met, add the string to the list
                strings.append(string)
    
    # Return the n-th string in the list, or -1 if it doesn't exist
    return strings[n-1] if n <= len(strings) else -1

