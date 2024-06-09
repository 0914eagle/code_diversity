
def solve(s, t):
    # Find the first occurrence of t in s
    start_index = s.find(t)
    # If t is not found in s, return 0
    if start_index == -1:
        return 0
    # Initialize the maximum length of the substring to remove
    max_length = 0
    # Iterate over the characters in t
    for i in range(len(t)):
        # Check if the substring s[start_index:start_index+i+1] is a subsequence of s
        if s[start_index:start_index+i+1] == t[:i+1]:
            # If it is, update the maximum length of the substring to remove
            max_length = max(max_length, i+1)
    # Return the maximum length of the substring to remove
    return max_length

