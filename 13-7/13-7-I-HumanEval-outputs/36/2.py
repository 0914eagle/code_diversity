
def solve(s: str) -> str:
    
    # Initialize an empty list to store the resulting string
    result = []
    
    # Iterate through the input string
    for char in s:
        # If the character is a letter, reverse its case
        if char.isalpha():
            result.append(char.swapcase())
        # Otherwise, keep the character as it is
        else:
            result.append(char)
    
    # If the resulting string is empty, reverse the input string
    if not result:
        result = s[::-1]
    
    # Return the resulting string
    return "".join(result)

