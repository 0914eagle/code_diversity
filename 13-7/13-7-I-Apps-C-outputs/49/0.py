
def solve(s):
    # Initialize an empty list to store the suffixes
    suffixes = []
    
    # Loop through the string and check if the substring is a suffix
    for i in range(len(s)):
        for j in range(i+2, len(s)+1):
            # Check if the substring is not the same as the original string
            if s[i:j] != s:
                # Add the substring to the list of suffixes
                suffixes.append(s[i:j])
    
    # Return the list of distinct suffixes
    return list(set(suffixes))

