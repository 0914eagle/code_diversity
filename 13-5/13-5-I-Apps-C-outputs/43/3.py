
import sys

sys.setrecursionlimit(10**6)

MOD = 1000000007

def shortest_paths(n, roads):
    graph = [[] for _ in range(n + 1)]
    for o, d, l in roads:
        graph[o].append((d, l))
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in graph[i]:
            dp[i] += dp[j[0]]
            dp[i] %= MOD
    
    return dp[n]

def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        o, d, l = map(int, input().split())
        roads.append((o, d, l))
    
    print(shortest_paths(n, roads))

if __name__ == '__main__':
    main()

