
def f1(n, m, roads, k, orders):
    # Your code here
    return max_wait_time

def f2(n, m, roads, k, orders):
    # Your code here
    return delivery_schedule

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
    print(f2(n, m, roads, k, orders))

