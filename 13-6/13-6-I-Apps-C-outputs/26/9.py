
def f1(n, m, w, h, volumes, x, min_sand, max_sand):
    # Your code here
    return ...

def f2(n, m, w, h, volumes, x, min_sand, max_sand):
    # Your code here
    return ...

if __name__ == '__main__':
    n, m, w, h = map(int, input().split())
    volumes = list(map(float, input().split()))
    x = list(map(float, input().split()))
    min_sand = []
    for i in range(n):
        min_sand.append(list(map(float, input().split())))
    max_sand = []
    for i in range(n):
        max_sand.append(list(map(float, input().split())))

    # Your code here
    ...

    print(round(f1(n, m, w, h, volumes, x, min_sand, max_sand), 3))

