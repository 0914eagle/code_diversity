
import sys

def count_substring(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

N = int(input())
T = input()

# Concatenate 10^10 copies of the string 110
S = "110" * (10**10)

# Count the number of times T occurs in S as a contiguous substring
count = count_substring(S, T)

print(count)

