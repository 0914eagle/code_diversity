
def f1(s):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(s)):
        # If the current character is 'm', check if the next two characters are 'e' and 'o'
        if s[i] == 'm':
            if i + 1 < len(s) and s[i + 1] == 'e' and i + 2 < len(s) and s[i + 2] == 'o':
                # If they are, increment the meow factor by 1
                meow_factor += 1
    
    # Return the meow factor
    return meow_factor

def f2(s):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(s)):
        # If the current character is 'm', check if the previous two characters are 'e' and 'o'
        if s[i] == 'm':
            if i - 1 >= 0 and s[i - 1] == 'e' and i - 2 >= 0 and s[i - 2] == 'o':
                # If they are, increment the meow factor by 1
                meow_factor += 1
    
    # Return the meow factor
    return meow_factor

def f3(s):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(s)):
        # If the current character is 'm', check if the next character is 'e'
        if s[i] == 'm':
            if i + 1 < len(s) and s[i + 1] == 'e':
                # If it is, increment the meow factor by 1
                meow_factor += 1
    
    # Return the meow factor
    return meow_factor

def f4(s):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(s)):
        # If the current character is 'm', check if the previous character is 'e'
        if s[i] == 'm':
            if i - 1 >= 0 and s[i - 1] == 'e':
                # If it is, increment the meow factor by 1
                meow_factor += 1
    
    # Return the meow factor
    return meow_factor

def main():
    # Read a string from stdin
    s = input()
    
    # Call the four functions and print the maximum meow factor
    print(max(f1(s), f2(s), f3(s), f4(s)))

if __name__ == '__main__':
    main()

