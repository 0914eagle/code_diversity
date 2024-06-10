
def solve(s):
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through the input string
    for i in range(len(s)):
        # If the current character is not '<', append it to the result
        if s[i] != "<":
            result += s[i]
        # If the current character is '<' and the next character is not '<', remove the last character from the result
        elif s[i] == "<" and i < len(s) - 1 and s[i+1] != "<":
            result = result[:-1]
    
    # Return the result
    return result

