
import itertools

def get_palindromic_strings(s):
    # Generate all possible palindromic strings of length 2*len(s)
    palindromes = itertools.product(s, repeat=len(s))
    
    # Filter out strings that don't contain s as a subsequence
    palindromes = filter(lambda x: s in ''.join(x), palindromes)
    
    # Return the count of palindromic strings
    return len(list(palindromes))

def get_number_of_palindromic_strings(s):
    # Get the number of palindromic strings of length 2*len(s) that contain s as a subsequence
    num_palindromes = get_palindromic_strings(s)
    
    # Return the result modulo 10^9+7
    return num_palindromes % (10**9+7)

if __name__ == '__main__':
    # Get the input string
    s = input()
    
    # Get the number of palindromic strings of length 2*len(s) that contain s as a subsequence
    num_palindromes = get_number_of_palindromic_strings(s)
    
    # Print the result
    print(num_palindromes)

