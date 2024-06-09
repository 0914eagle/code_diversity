
import sys

def get_gis(g):
    gis = []
    for i in range(len(g)):
        if i == 0:
            gis.append(g[i])
        else:
            for j in range(i, len(g)):
                if g[j] > g[i-1]:
                    gis.append(g[j])
                    break
    return gis

def count_permutations(n, gis):
    mod = 1000000007
    dp = [1] * (n+1)
    for i in range(1, len(gis)):
        for j in range(gis[i-1], n+1):
            dp[j] += dp[j-1]
            dp[j] %= mod
    return dp[n]

n, l = map(int, input().split())
g = list(map(int, input().split()))
gis = get_gis(g)
print(count_permutations(n, gis))

