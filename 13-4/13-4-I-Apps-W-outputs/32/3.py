
import sys

def get_gis(g, n):
    gis = []
    for i in range(len(g)):
        gis.append(g[i])
        for j in range(i+1, len(g)):
            if g[i] < g[j]:
                gis.append(g[j])
                break
    gis.sort()
    return gis

def count_permutations(g, n):
    gis = get_gis(g, n)
    count = 1
    for i in range(len(gis)):
        count *= n - i
    return count % (10**9 + 7)

if __name__ == '__main__':
    n, l = map(int, input().split())
    g = list(map(int, input().split()))
    print(count_permutations(g, n))

