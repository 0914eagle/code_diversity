
def meow_factor(s):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the current character is 'm'
        if s[i] == 'm':
            # If it is, check if the next three characters are 'e', 'o', and 'w'
            if i + 1 < len(s) and s[i + 1] == 'e' and i + 2 < len(s) and s[i + 2] == 'o' and i + 3 < len(s) and s[i + 3] == 'w':
                # If they are, return the current meow factor
                return meow_factor
        # If the current character is not 'm', increment the meow factor
        meow_factor += 1
    
    # If the word "meow" is not found in the string, return -1
    return -1

