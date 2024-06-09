
import sys

def solve(L, R):
    count = 0
    for i in range(L, R+1):
        if '4' in str(i):
            continue
        sixes = eights = 0
        for j in str(i):
            if j == '6':
                sixes += 1
            elif j == '8':
                eights += 1
        if sixes == eights:
            count += 1
    return count % (10**9+7)

L, R = map(int, input().split())
print(solve(L, R))

