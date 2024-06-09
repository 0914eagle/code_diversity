
def f1(n, s):
    # Calculate the number of palindromic strings of length 2n
    num_palindromes = (2 * n) * (2 * n + 1) // 2
    
    # Initialize a dictionary to store the count of palindromes with each letter
    letter_counts = {}
    for letter in s:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
    
    # Subtract the number of palindromes with each letter that is not in S
    for letter in letter_counts:
        if letter not in s:
            num_palindromes -= letter_counts[letter]
    
    # Return the result modulo 10^9+7
    return num_palindromes % 1000000007

def f2(n, s):
    # Calculate the number of palindromic strings of length 2n that contain S as a subsequence
    num_palindromes = 0
    for i in range(n):
        # Get the ith letter of S
        letter = s[i]
        
        # Calculate the number of palindromes of length 2n that start with letter
        num_palindromes += f1(n, letter)
    
    # Return the result modulo 10^9+7
    return num_palindromes % 1000000007

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f2(n, s))

