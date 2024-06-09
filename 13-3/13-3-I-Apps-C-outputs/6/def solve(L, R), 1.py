
import sys

def solve(L, R):
    count = 0
    for i in range(L, R+1):
        num_6 = 0
        num_8 = 0
        for j in str(i):
            if j == '6':
                num_6 += 1
            elif j == '8':
                num_8 += 1
            elif j == '4':
                break
        if num_6 == num_8:
            count += 1
    return count % (10**9+7)

L, R = map(int, input().split())
print(solve(L, R))

