
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

def count_permutations(n, g):
    gis = get_gis(g)
    count = 1
    for i in range(len(gis)):
        count *= n - i
    return count % (10**9 + 7)

n, l = map(int, input().split())
g = list(map(int, input().split()))
print(count_permutations(n, g))

