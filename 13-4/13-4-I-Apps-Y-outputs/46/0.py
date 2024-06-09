
def f1(s, n):
    # Convert the input string to a list of characters
    char_list = list(s)
    
    # Loop through each character in the list
    for i in range(len(char_list)):
        # Calculate the new position of the character based on the shift value
        new_pos = (ord(char_list[i]) - ord('A') + n) % 26
        
        # Update the character at the new position
        char_list[i] = chr(ord('A') + new_pos)
    
    # Return the updated string
    return "".join(char_list)

def f2(s, n):
    # Split the input string into a list of characters
    char_list = list(s)
    
    # Loop through each character in the list
    for i in range(len(char_list)):
        # Calculate the new position of the character based on the shift value
        new_pos = (ord(char_list[i]) - ord('A') + n) % 26
        
        # Update the character at the new position
        char_list[i] = chr(ord('A') + new_pos)
    
    # Return the updated string
    return "".join(char_list)

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(s, n))
    print(f2(s, n))

