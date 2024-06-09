
def read_input():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, a, edges

def get_cost(n, a, edges, v):
    cost = 0
    for i in range(1, n + 1):
        cost += dist(i, v, edges) * a[i - 1]
    return cost

def dist(i, j, edges):
    for u, v in edges:
        if i == u and j == v or i == v and j == u:
            return 1
    return 0

def get_max_cost(n, a, edges):
    max_cost = 0
    for v in range(1, n + 1):
        cost = get_cost(n, a, edges, v)
        max_cost = max(max_cost, cost)
    return max_cost

def main():
    n, a, edges = read_input()
    print(get_max_cost(n, a, edges))

if __name__ == '__main__':
    main()

