
def f1(s, n):
    # Convert the input string to a list of characters
    char_list = list(s)
    
    # Loop through each character in the list
    for i in range(len(char_list)):
        # Calculate the new position of the character based on the shift value
        new_pos = (ord(char_list[i]) - ord('A') + n) % 26
        
        # Update the character at the new position
        char_list[i] = chr(ord('A') + new_pos)
    
    # Join the list of characters into a string and return it
    return "".join(char_list)

def f2():
    # Read the input from stdin
    n = int(input())
    s = input()
    
    # Call the first function with the input parameters
    result = f1(s, n)
    
    # Print the result to stdout
    print(result)

if __name__ == '__main__':
    f2()

