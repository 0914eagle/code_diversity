
def solve(s, n):
    # Convert the input string to a list of characters
    char_list = list(s)
    
    # Loop through each character in the list
    for i in range(len(char_list)):
        # Calculate the new index of the character after shifting by N
        new_index = (ord(char_list[i]) - ord('A') + n) % 26
        
        # Update the character at the new index
        char_list[i] = chr(ord('A') + new_index)
    
    # Join the list of characters back into a string
    return "".join(char_list)

