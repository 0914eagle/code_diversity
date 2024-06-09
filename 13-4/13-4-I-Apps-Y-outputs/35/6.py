
def solve(n, k):
    # Initialize a list to store the letters of the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize an empty string to store the result
    result = ""
    
    # Loop through each letter of the alphabet
    for letter in alphabet:
        # Check if the letter is in the string
        if letter in result:
            # If the letter is already in the string, continue to the next letter
            continue
        # Check if the letter is in the first k letters of the string
        if letter in result[:k]:
            # If the letter is in the first k letters of the string, add it to the result and continue to the next letter
            result += letter
        # Check if the letter is in the last n-k letters of the string
        if letter in result[-k:]:
            # If the letter is in the last n-k letters of the string, add it to the result and continue to the next letter
            result += letter
    
    # Return the result
    return result

