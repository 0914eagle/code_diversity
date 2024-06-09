
def solve(k, n):
    # Initialize a list to store the results
    results = []

    # Iterate over all possible strings
    for i in range(26**k):
        # Convert the current number to a string
        s = str(i)

        # Pad the string with leading zeros
        s = s.zfill(k)

        # Check if the string is double free
        if is_double_free(s):
            # Check if the string is k-incremental
            if is_k_incremental(s, k):
                # Add the string to the results list
                results.append(s)

    # Return the n-th string in the results list, or -1 if it doesn't exist
    return results[n-1] if n <= len(results) else -1

# Check if a string is double free
def is_double_free(s):
    # Iterate over the characters in the string
    for i in range(len(s) - 1):
        # Check if the current character is the same as the next character
        if s[i] == s[i+1]:
            # If it is, return False
            return False

    # If we reach this point, the string is double free
    return True

# Check if a string is k-incremental
def is_k_incremental(s, k):
    # Initialize a dictionary to store the frequency of each character
    freq = {}

    # Iterate over the characters in the string
    for c in s:
        # If the character is not already in the dictionary, add it with a frequency of 1
        if c not in freq:
            freq[c] = 1
        # Otherwise, increment the frequency of the character
        else:
            freq[c] += 1

    # Check if the frequency of each character is k-incremental
    for c in freq:
        # If the frequency is not k-incremental, return False
        if freq[c] != k:
            return False

    # If we reach this point, the string is k-incremental
    return True

