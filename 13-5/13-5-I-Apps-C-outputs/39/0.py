
import sys

def solve(L, R):
    count = 0
    for num in range(L, R+1):
        num_str = str(num)
        if '4' in num_str:
            continue
        sixes = eightes = 0
        for digit in num_str:
            if digit == '6':
                sixes += 1
            elif digit == '8':
                eightes += 1
        if sixes == eightes:
            count += 1
    return count % (10**9+7)

L, R = map(int, input().split())
print(solve(L, R))

