
def get_input():
    n, m, w, h = map(int, input().split())
    volumes = list(map(float, input().split()))
    x = list(map(float, input().split()))
    min_sand = [[0] * m for _ in range(n)]
    max_sand = [[0] * m for _ in range(n)]
    for i in range(n):
        min_sand[i] = list(map(float, input().split()))
        max_sand[i] = list(map(float, input().split()))
    return n, m, w, h, volumes, x, min_sand, max_sand

def f1(n, m, w, h, volumes, x, min_sand, max_sand):
    # implement your solution here
    return 0

def f2(n, m, w, h, volumes, x, min_sand, max_sand):
    # implement your solution here
    return 0

if __name__ == '__main__':
    n, m, w, h, volumes, x, min_sand, max_sand = get_input()
    print(f1(n, m, w, h, volumes, x, min_sand, max_sand))
    print(f2(n, m, w, h, volumes, x, min_sand, max_sand))

