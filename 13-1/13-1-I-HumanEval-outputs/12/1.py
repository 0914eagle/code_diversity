
def solve(s: str) -> str:
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through the characters of the input string
    for char in s:
        # If the character is a letter, reverse its case
        if char.isalpha():
            result += char.swapcase()
        # Otherwise, keep the character as it is
        else:
            result += char
    
    # If the string contains no letters, reverse the string
    if not any(char.isalpha() for char in s):
        result = result[::-1]
    
    return result

