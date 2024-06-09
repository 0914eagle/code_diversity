
def solve(s, n):
    # Convert input string to uppercase
    s = s.upper()
    
    # Initialize result string
    result = ""
    
    # Loop through each character in the input string
    for char in s:
        # Calculate the new character position based on the shift value
        new_pos = (ord(char) - ord('A') + n) % 26
        
        # Add the new character to the result string
        result += chr(ord('A') + new_pos)
    
    # Return the result string
    return result

