
import sys

def solve(s):
    mod = 10**9+7
    count = 0
    for i in range(len(s)):
        if s[i] == '?':
            for j in range(10):
                num = int(s[:i] + str(j) + s[i+1:])
                if num % 13 == 5:
                    count += 1
                    count %= mod
        else:
            num = int(s)
            if num % 13 == 5:
                count += 1
                count %= mod
    return count

s = input()
print(solve(s))

