
def f1(n, m, q):
    # f1 should return a list of lists, where the inner list contains the cost of sending a crystal from city s to city t on each day
    return [[0] * q for _ in range(n)]

def f2(n, m, q):
    # f2 should return a list of lists, where the inner list contains the cost of sending a crystal from city s to city t on each day
    return [[0] * q for _ in range(n)]

if __name__ == '__main__':
    n, m = map(int, input().split())
    q = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a - 1].append((b - 1, w))
        graph[b - 1].append((a - 1, w))
    costs = f1(n, m, q)
    for i in range(q):
        s, t = map(int, input().split())
        costs[s - 1][i] = f2(s - 1, t - 1, graph)
    for cost in costs:
        print(*cost)

