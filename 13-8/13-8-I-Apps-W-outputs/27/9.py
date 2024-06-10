
def get_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        x, y = map(int, input().split())
        roads.append((x, y))
    return n, m, a, roads

def get_f(p, q, a, roads):
    f = 0
    for i in range(len(roads)):
        x, y = roads[i]
        if x == p and y == q:
            f = max(f, a[x])
        elif x == q and y == p:
            f = max(f, a[y])
    return f

def get_average_f(n, m, a, roads):
    total = 0
    for p in range(1, n + 1):
        for q in range(1, n + 1):
            if p != q:
                f = get_f(p, q, a, roads)
                total += f
    return total / (n * (n - 1))

def main():
    n, m, a, roads = get_input()
    average = get_average_f(n, m, a, roads)
    print(average)

if __name__ == '__main__':
    main()

