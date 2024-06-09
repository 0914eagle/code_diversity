
import math
import random

def get_input():
    n = int(input())
    trees = []
    for i in range(n):
        x, y, r = map(int, input().split())
        trees.append((x, y, r))
    b, d = map(int, input().split())
    return n, trees, b, d

def circle_overlap(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return d < r1 + r2

def boar_charge(b, d, trees):
    x, y, r = 0, 0, b
    while d > 0:
        theta = random.uniform(0, 2*math.pi)
        dx = math.cos(theta) * d
        dy = math.sin(theta) * d
        x += dx
        y += dy
        d -= dx
        for tree in trees:
            if circle_overlap(x, y, r, tree[0], tree[1], tree[2]):
                return False
    return True

def f1(n, trees, b, d):
    return boar_charge(b, d, trees)

def f2(n, trees, b, d):
    return 1 - f1(n, trees, b, d)

if __name__ == '__main__':
    n, trees, b, d = get_input()
    print(f2(n, trees, b, d))

