
def get_input():
    n, m, w, h = map(int, input().split())
    assert 2 <= n <= 200 and 1 <= m <= 200 and 1 <= w <= 5000 and 1 <= h <= 5000

    volumes = list(map(float, input().split()))
    assert len(volumes) == m and all(0 < v <= w * h for v in volumes)

    x_coords = list(map(float, input().split()))
    assert len(x_coords) == n - 1 and all(0 < x < w for x in x_coords)
    assert sorted(x_coords) == x_coords

    min_sand = []
    for i in range(n):
        min_sand.append(list(map(float, input().split())))
    assert all(len(row) == m and all(0 <= v <= w * h for v in row) for row in min_sand)

    max_sand = []
    for i in range(n):
        max_sand.append(list(map(float, input().split())))
    assert all(len(row) == m and all(0 <= v <= w * h for v in row) and all(min_sand[i][j] <= max_sand[i][j] for j in range(m)) for i in range(n))

    return n, m, w, h, volumes, x_coords, min_sand, max_sand

def f1(n, m, w, h, volumes, x_coords, min_sand, max_sand):
    # your code here
    pass

def f2(n, m, w, h, volumes, x_coords, min_sand, max_sand):
    # your code here
    pass

if __name__ == '__main__':
    n, m, w, h, volumes, x_coords, min_sand, max_sand = get_input()
    print(f1(n, m, w, h, volumes, x_coords, min_sand, max_sand))
    print(f2(n, m, w, h, volumes, x_coords, min_sand, max_sand))

