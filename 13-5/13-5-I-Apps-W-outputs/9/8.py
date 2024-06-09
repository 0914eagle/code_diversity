
def f1(s):
    # Initialize a set to store the unique strings
    unique_strings = set()
    
    # Add the initial string to the set
    unique_strings.add(s)
    
    # Loop for each character in the string
    for i in range(len(s)):
        # Get the substring starting from the ith character
        substring = s[i:] + s[:i]
        
        # Add the substring to the set if it is not already present
        if substring not in unique_strings:
            unique_strings.add(substring)
    
    # Return the length of the set
    return len(unique_strings)

