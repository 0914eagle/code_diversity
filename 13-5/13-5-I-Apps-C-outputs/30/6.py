
def f1(n, m, roads, k, orders):
    # f1 should return the longest time a customer has to wait from the time they place their order until the order is delivered, assuming that Holly uses a delivery schedule minimizing this value.
    return 0

def f2(...):
    # f2 should be a helper function for f1
    return ...

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        roads.append((u, v, d))
    k = int(input())
    orders = []
    for _ in range(k):
        s, u, t = map(int, input().split())
        orders.append((s, u, t))
    print(f1(n, m, roads, k, orders))

