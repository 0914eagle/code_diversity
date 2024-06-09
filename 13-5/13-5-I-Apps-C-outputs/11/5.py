
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

def is_overlapping(x1, y1, r1, x2, y2, r2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r1 + r2

def is_hit(x, y, r, trees):
    for tree in trees:
        if is_overlapping(x, y, r, tree[0], tree[1], tree[2]):
            return True
    return False

def simulate(n, trees, b, d):
    count = 0
    for i in range(100000):
        x = random.uniform(-10**6, 10**6)
        y = random.uniform(-10**6, 10**6)
        if is_hit(x, y, b, trees):
            continue
        x += d*math.cos(random.uniform(0, 2*math.pi))
        y += d*math.sin(random.uniform(0, 2*math.pi))
        if is_hit(x, y, b, trees):
            count += 1
    return count/100000

def main():
    n, trees, b, d = get_input()
    print(simulate(n, trees, b, d))

if __name__ == '__main__':
    main()

