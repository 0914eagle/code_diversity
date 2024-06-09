
def solve(s: str) -> str:
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate through the string
    for char in s:
        # If the character is a letter, reverse its case
        if char.isalpha():
            result.append(char.swapcase())
        # Otherwise, keep the character as it is
        else:
            result.append(char)
    
    # If the string contains no letters, reverse the string
    if not any(char.isalpha() for char in s):
        result.reverse()
    
    # Return the resulted string
    return "".join(result)

