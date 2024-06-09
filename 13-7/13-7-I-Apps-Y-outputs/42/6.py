
def solve(s, t):
    # Find the first occurrence of t in s
    start_index = s.find(t)
    # If t is not found in s, return 0
    if start_index == -1:
        return 0
    # Initialize the maximum length of the substring to remove
    max_length = 0
    # Iterate over the characters of t
    for i in range(len(t)):
        # Check if the substring starting at start_index and ending at start_index + i is a subsequence of s
        substring = s[start_index:start_index+i+1]
        if t == substring:
            # If it is a subsequence, update the maximum length
            max_length = max(max_length, i+1)
    # Return the maximum length
    return max_length

