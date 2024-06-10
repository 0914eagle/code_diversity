
import sys

def get_meow_factor(s):
    # Initialize the meow factor to 0
    meow_factor = 0
    
    # Iterate through the string and check if "meow" is a substring
    for i in range(len(s) - 2):
        if s[i:i+3] == "meo":
            # If "meow" is a substring, increment the meow factor by 1
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

