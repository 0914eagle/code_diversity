
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

def intersects(x1, y1, r1, x2, y2, r2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r1 + r2

def charge(x, y, b, d, trees):
    while d > 0:
        theta = random.uniform(0, 2*math.pi)
        dx = math.cos(theta) * d
        dy = math.sin(theta) * d
        x += dx
        y += dy
        d -= dx
        for tree in trees:
            if intersects(x, y, b, tree[0], tree[1], tree[2]):
                return False
    return True

def f1(n, trees, b, d):
    count = 0
    for i in range(10000):
        x, y = 0, 0
        if charge(x, y, b, d, trees):
            count += 1
    return count / 10000

def f2(n, trees, b, d):
    count = 0
    for i in range(10000):
        x, y = random.uniform(-10**6, 10**6), random.uniform(-10**6, 10**6)
        if charge(x, y, b, d, trees):
            count += 1
    return count / 10000

if __name__ == '__main__':
    n, trees, b, d = get_input()
    print(f1(n, trees, b, d))
    print(f2(n, trees, b, d))

