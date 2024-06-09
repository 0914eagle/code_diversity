
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

def overlaps(tree, boar):
    x, y, r = tree
    bx, by, br = boar
    return (x - bx) ** 2 + (y - by) ** 2 <= (r + br) ** 2

def charge(boar, trees, d):
    x, y, r = boar
    dx, dy = random.uniform(-1, 1), random.uniform(-1, 1)
    while d > 0:
        x += dx
        y += dy
        d -= 1
        if any(overlaps(tree, (x, y, r)) for tree in trees):
            return False
    return True

def f1(n, trees, b, d):
    total = 0
    for i in range(10000):
        boar = (0, 0, b)
        if charge(boar, trees, d):
            total += 1
    return total / 10000

def f2(n, trees, b, d):
    total = 0
    for i in range(10000):
        boar = (0, 0, b)
        if charge(boar, trees, d):
            total += 1
    return total / 10000

if __name__ == '__main__':
    n, trees, b, d = get_input()
    print(f1(n, trees, b, d))
    print(f2(n, trees, b, d))

