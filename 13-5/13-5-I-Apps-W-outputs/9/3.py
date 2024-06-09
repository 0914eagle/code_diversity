
def f1(s):
    # Initialize a set to store the distinct strings
    distinct_strings = set()
    
    # Add the initial string to the set
    distinct_strings.add(s)
    
    # Loop for each character in the string
    for i in range(len(s)):
        # Get the substring starting from the current index and ending at the end of the string
        substring = s[i:]
        
        # Add the substring to the set
        distinct_strings.add(substring)
        
        # Get the substring starting from the beginning of the string and ending at the current index - 1
        substring = s[:i]
        
        # Add the substring to the set
        distinct_strings.add(substring)
    
    # Return the length of the set
    return len(distinct_strings)

