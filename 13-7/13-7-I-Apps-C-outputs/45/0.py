
def meow_factor(s):
    # Initialize the meow factor to 0
    meow_f = 0

    # Loop through each character in the string
    for i in range(len(s)):
        # If the current character is 'm', check if the next three characters are 'e', 'o', and 'w'
        if s[i] == 'm':
            if i + 1 < len(s) and s[i + 1] == 'e' and i + 2 < len(s) and s[i + 2] == 'o' and i + 3 < len(s) and s[i + 3] == 'w':
                # If so, return the current meow factor
                return meow_f
        # If the current character is not 'm', increment the meow factor
        else:
            meow_f += 1

    # If the string does not contain the word "meow", return -1
    return -1

