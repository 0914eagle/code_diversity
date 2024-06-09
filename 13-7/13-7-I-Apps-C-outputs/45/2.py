
def meow_factor(s):
    # Initialize the meow factor to 0
    meow_factor = 0
    # Loop through each character in the string
    for i in range(len(s)):
        # If the character is 'm', increment the meow factor
        if s[i] == 'm':
            meow_factor += 1
        # If the character is 'e', increment the meow factor
        if s[i] == 'e':
            meow_factor += 1
        # If the character is 'o', increment the meow factor
        if s[i] == 'o':
            meow_factor += 1
        # If the character is 'w', increment the meow factor
        if s[i] == 'w':
            meow_factor += 1
    # Return the meow factor
    return meow_factor

