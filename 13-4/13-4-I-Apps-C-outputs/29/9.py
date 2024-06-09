
def get_palindromes(s):
    # Initialize an empty list to store the palindromes
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
    # Get all possible palindromes in the string
    palindromes = get_palindromes(s)
    
    # Initialize a variable to store the minimum number of palindromes
    min_palindromes = len(s)
    
    # Loop through each possible combination of palindromes
    for i in range(1, len(palindromes) + 1):
        # Check if the combination of palindromes is a valid solution
        if is_valid_solution(palindromes, i):
            # If it is, update the minimum number of palindromes
            min_palindromes = min(min_palindromes, i)
    
    return min_palindromes

def is_valid_solution(palindromes, k):
    # Check if the combination of palindromes is a valid solution
    return len(set(len(p) for p in palindromes[:k])) == 1

def main():
    # Read the input string
    s = input()
    
    # Get the minimum number of palindromes
    min_palindromes = get_min_palindromes(s)
    
    # Print the minimum number of palindromes
    print(min_palindromes)
    
    # Print the palindromes
    for i in range(min_palindromes):
        print(palindromes[i], end=" ")

if __name__ == '__main__':
    main()

