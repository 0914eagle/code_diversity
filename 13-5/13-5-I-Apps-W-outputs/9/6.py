
def f1(s):
    # Initialize a set to store the distinct strings
    distinct_strings = set()
    
    # Add the initial string to the set
    distinct_strings.add(s)
    
    # Loop for each character in the string
    for i in range(len(s)):
        # Get the substring starting from the current character
        substring = s[i:] + s[:i]
        
        # Add the substring to the set if it is not already present
        if substring not in distinct_strings:
            distinct_strings.add(substring)
    
    # Return the number of distinct strings
    return len(distinct_strings)

