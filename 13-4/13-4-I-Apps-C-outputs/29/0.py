
def get_palindromes(s):
    # Initialize an empty list to store the palindromes
    palindromes = []
    
    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the character is a palindrome
        if s[i] == s[len(s) - i - 1]:
            # If it is a palindrome, add it to the list of palindromes
            palindromes.append(s[i])
    
    # Return the list of palindromes
    return palindromes

def get_min_palindromes(s):
    # Get all the palindromes in the string
    palindromes = get_palindromes(s)
    
    # Initialize a variable to store the minimum number of palindromes
    min_palindromes = len(palindromes)
    
    # Loop through each palindrome and check if it is a prefix of the string
    for palindrome in palindromes:
        # Check if the palindrome is a prefix of the string
        if s.startswith(palindrome):
            # If it is a prefix, remove the prefix from the string and recurse
            min_palindromes = min(min_palindromes, get_min_palindromes(s[len(palindrome):]))
    
    # Return the minimum number of palindromes
    return min_palindromes

def main():
    # Read the input string
    s = input()
    
    # Get the minimum number of palindromes
    min_palindromes = get_min_palindromes(s)
    
    # Print the minimum number of palindromes
    print(min_palindromes)
    
    # Get the palindromes
    palindromes = get_palindromes(s)
    
    # Print the palindromes
    print(" ".join(palindromes))

if __name__ == '__main__':
    main()

