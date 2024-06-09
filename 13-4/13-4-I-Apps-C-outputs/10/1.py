
import sys

def count_distinct_strings(s):
    n = len(s)
    if n == 1:
        return 1
    else:
        count = 0
        for i in range(n-1):
            if s[i] != s[i+1]:
                count += count_distinct_strings(s[:i] + s[i+2:])
        return count

n = int(input())
s = input()
print(count_distinct_strings(s) % (10**9 + 7))

