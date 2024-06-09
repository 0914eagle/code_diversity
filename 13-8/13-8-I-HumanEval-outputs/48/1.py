
def solve(s: str) -> str:
    
    # Initialize a flag to keep track of whether any letters are found in the string
    letters_found = False
    # Iterate through the string and check if each character is a letter
    for i in range(len(s)):
        if s[i].isalpha():
            # If a letter is found, set the flag to True
            letters_found = True
            # And toggle the case of the letter
            s = s[:i] + s[i].swapcase() + s[i+1:]
    # If no letters were found, reverse the string
    if not letters_found:
        s = s[::-1]
    return s

