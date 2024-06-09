
import sys

def solve(s):
    mod = 10**9+7
    count = 0
    for i in range(len(s)):
        if s[i] == '?':
            for j in range(10):
                s_new = s[:i] + str(j) + s[i+1:]
                if int(s_new) % 13 == 5:
                    count += 1
                    count %= mod
    return count

s = sys.stdin.readline().strip()
print(solve(s))

