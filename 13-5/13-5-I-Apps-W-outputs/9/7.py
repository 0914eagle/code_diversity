
def f1(s):
    # Initialize a set to store the distinct strings
    distinct_strings = set()
    
    # Add the initial string to the set
    distinct_strings.add(s)
    
    # Loop for each character in the string
    for i in range(len(s)):
        # Cyclically shift the string by 1 character
        shifted_string = s[1:] + s[0]
        
        # Add the shifted string to the set if it is not already present
        if shifted_string not in distinct_strings:
            distinct_strings.add(shifted_string)
    
    # Return the number of distinct strings
    return len(distinct_strings)

