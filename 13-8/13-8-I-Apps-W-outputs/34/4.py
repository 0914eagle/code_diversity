
def solve(s):
    n = len(s)
    # Initialize the smallest string and its corresponding k value
    smallest_string = s
    smallest_k = 1
    # Iterate through all possible values of k
    for k in range(1, n + 1):
        # Create a copy of the original string
        modified_string = s[:]
        # Iterate through all substrings of length k
        for i in range(n - k + 1):
            # Reverse the substring
            modified_string = modified_string[:i] + modified_string[i:i + k][::-1] + modified_string[i + k:]
        # If the modified string is lexicographically smaller than the current smallest string, update the smallest string and its corresponding k value
        if modified_string < smallest_string:
            smallest_string = modified_string
            smallest_k = k
    # Return the smallest string and its corresponding k value
    return smallest_string, smallest_k

