
import math
import random

def is_overlapping(x1, y1, r1, x2, y2, r2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r1 + r2

def simulate_charge(trees, boar_radius, distance):
    boar_x, boar_y = 0, 0
    direction = random.uniform(0, 2*math.pi)
    step_size = distance / 100
    for i in range(100):
        boar_x += step_size * math.cos(direction)
        boar_y += step_size * math.sin(direction)
        for tree in trees:
            if is_overlapping(boar_x, boar_y, boar_radius, tree[0], tree[1], tree[2]):
                return False
    return True

def f1(n, *args):
    trees = []
    for i in range(n):
        x, y, r = map(float, input().split())
        trees.append((x, y, r))
    b, d = map(float, input().split())
    return simulate_charge(trees, b, d)

def f2(...):
    ...

if __name__ == '__main__':
    f1(...)

