
import sys

def solve(L, R):
    count = 0
    for i in range(L, R+1):
        str_i = str(i)
        if '4' in str_i:
            continue
        six_count = eight_count = 0
        for j in str_i:
            if j == '6':
                six_count += 1
            elif j == '8':
                eight_count += 1
        if six_count == eight_count:
            count += 1
    return count % (10**9+7)

L, R = map(int, input().split())
print(solve(L, R))

