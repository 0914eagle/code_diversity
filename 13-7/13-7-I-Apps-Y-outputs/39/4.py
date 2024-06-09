
def solve(s, n):
    # Convert the input string to a list of characters
    char_list = list(s)
    
    # Loop through each character in the list
    for i in range(len(char_list)):
        # Calculate the new index of the character by adding the shift value
        new_index = (ord(char_list[i]) - ord('A') + n) % 26
        
        # Replace the character at the current index with the new character
        char_list[i] = chr(ord('A') + new_index)
    
    # Join the list of characters back into a string and return it
    return "".join(char_list)

