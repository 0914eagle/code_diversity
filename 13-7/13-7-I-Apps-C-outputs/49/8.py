
def solve(s):
    # Initialize an empty list to store the suffixes
    suffixes = []
    
    # Loop through the string and check if the substring is a suffix
    for i in range(len(s)):
        for j in range(i+2, len(s)+1):
            # Check if the substring is not already in the list of suffixes
            if s[i:j] not in suffixes:
                # Add the substring to the list of suffixes
                suffixes.append(s[i:j])
    
    # Return the list of suffixes
    return suffixes

