
import sys

def f1(n, s):
    # Calculate the number of palindromic strings of length 2n that contain s as a subsequence
    count = 0
    for i in range(len(s)):
        # Check if the substring s[i:i+n] is a palindrome
        if s[i:i+n] == s[i:i+n][::-1]:
            count += 1
    return count

def f2(n, s):
    # Calculate the number of palindromic strings of length 2n that contain s as a subsequence and are not contiguous
    count = 0
    for i in range(len(s)):
        # Check if the substring s[i:i+n] is a palindrome
        if s[i:i+n] == s[i:i+n][::-1]:
            # Check if the substring s[i:i+n] is contiguous in s
            if s.find(s[i:i+n], i+1) == -1:
                count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(n, s))
    print(f2(n, s))

