
def solve(s):
    # Initialize a set to store the generated strings
    generated_strings = set()
    
    # Add the initial string to the set
    generated_strings.add(s)
    
    # Loop for each character in the string
    for i in range(len(s)):
        # Generate a new string by moving the last character to the beginning
        new_string = s[i:] + s[:i]
        
        # If the new string is not already in the set, add it to the set
        if new_string not in generated_strings:
            generated_strings.add(new_string)
    
    # Return the length of the set, which is the number of distinct strings generated
    return len(generated_strings)

