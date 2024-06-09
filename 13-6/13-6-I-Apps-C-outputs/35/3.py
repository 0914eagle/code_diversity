
def get_meow_factor(s):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Loop through each character in the string
    for i in range(len(s)):
        # If the current character is 'm', check if the next three characters are 'e', 'o', and 'w'
        if s[i] == 'm' and s[i+1:i+4] == 'eow':
            # If they are, increment the meow factor by 1
            meow_factor += 1
    
    # Return the meow factor
    return meow_factor

def main():
    # Read a single line of input from stdin and convert it to a string
    s = input().strip()
    
    # Print the meow factor of the string
    print(get_meow_factor(s))

if __name__ == '__main__':
    main()

