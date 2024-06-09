
def get_palindromes(s):
    # Initialize a list to store the palindromes
    palindromes = []
    
    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the character is already in the palindromes list
        if s[i] not in palindromes:
            # If not, check if the character is a palindrome
            if is_palindrome(s[i:]):
                # If it is, add it to the palindromes list
                palindromes.append(s[i])
    
    return palindromes

def is_palindrome(s):
    # Check if the string is a palindrome
    return s == s[::-1]

def get_min_palindromes(s):
    # Get all the palindromes in the string
    palindromes = get_palindromes(s)
    
    # Initialize a variable to store the minimum number of palindromes
    min_palindromes = len(palindromes)
    
    # Loop through each palindrome
    for palindrome in palindromes:
        # Check if the palindrome is a substring of the string
        if s.find(palindrome) != -1:
            # If it is, remove it from the string
            s = s.replace(palindrome, "")
            # Decrement the minimum number of palindromes
            min_palindromes -= 1
    
    return min_palindromes

def main():
    # Read the input string
    s = input()
    
    # Get the minimum number of palindromes
    min_palindromes = get_min_palindromes(s)
    
    # Print the result
    print(min_palindromes)

if __name__ == '__main__':
    main()

