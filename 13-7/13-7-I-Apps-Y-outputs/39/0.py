
def solve(s, n):
    # Convert input string to uppercase
    s = s.upper()
    
    # Initialize result string
    result = ""
    
    # Iterate through each character of input string
    for c in s:
        # Calculate the shifted character
        shifted_char = chr((ord(c) - ord("A") + n) % 26 + ord("A"))
        
        # Add the shifted character to the result string
        result += shifted_char
    
    return result

