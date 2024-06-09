
def get_input():
    n, m, w, h = map(int, input().split())
    assert 2 <= n <= 200 and 1 <= m <= 200 and 1 <= w <= 5000 and 1 <= h <= 5000

    volumes = list(map(float, input().split()))
    assert len(volumes) == m and all(0 < v <= w * h for v in volumes)

    x = list(map(float, input().split()))
    assert len(x) == n - 1 and all(0 < xi < w for xi in x) and x == sorted(x)

    mins = [list(map(float, input().split())) for _ in range(n)]
    assert all(len(row) == m and all(0 <= min <= w * h for min in row) for row in mins)

    maxs = [list(map(float, input().split())) for _ in range(n)]
    assert all(len(row) == m and all(0 <= max <= w * h for max in row) and all(min <= max for row in zip(mins, maxs)) for row in maxs)

    return n, m, w, h, volumes, x, mins, maxs

def f1(n, m, w, h, volumes, x, mins, maxs):
    # implement your solution here
    pass

def f2(n, m, w, h, volumes, x, mins, maxs):
    # implement your solution here
    pass

if __name__ == '__main__':
    n, m, w, h, volumes, x, mins, maxs = get_input()
    print(f1(n, m, w, h, volumes, x, mins, maxs))
    print(f2(n, m, w, h, volumes, x, mins, maxs))

