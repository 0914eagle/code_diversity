
def get_max_palindromes(strings):
    # Initialize a variable to store the maximum number of palindromes
    max_palindromes = 0
    
    # Loop through each string
    for string in strings:
        # Check if the string is already palindrome
        if string == string[::-1]:
            # If it is, increment the maximum number of palindromes
            max_palindromes += 1
    
    # Return the maximum number of palindromes
    return max_palindromes

