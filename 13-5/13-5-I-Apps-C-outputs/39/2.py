
import sys

def is_palindrome(s):
    return s == s[::-1]

def count_palindromes(s, n):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if is_palindrome(s[i:j+1]):
                count += 1
    return count

def solve(s):
    n = len(s)
    return count_palindromes(s, n)

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(solve(s))

