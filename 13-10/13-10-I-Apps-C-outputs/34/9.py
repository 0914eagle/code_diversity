
import itertools

def get_palindromic_strings(n, s):
    
    # Generate all possible strings of length 2n
    strings = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=2*n)
    
    # Filter out strings that are not palindromic or do not contain s as a subsequence
    palindromic_strings = []
    for string in strings:
        if string == string[::-1] and s in ''.join(string):
            palindromic_strings.append(''.join(string))
    
    return palindromic_strings

def count_palindromic_strings(n, s):
    
    return len(get_palindromic_strings(n, s))

def main():
    n = int(input())
    s = input()
    print(count_palindromic_strings(n, s))

if __name__ == '__main__':
    main()

