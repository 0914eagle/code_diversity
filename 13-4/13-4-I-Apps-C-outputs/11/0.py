
import math

def get_input():
    n = int(input())
    fruits = []
    for i in range(n):
        x, y = map(float, input().split())
        fruits.append((x, y))
    return n, fruits

def get_slices(fruits):
    slices = []
    for i in range(len(fruits)):
        for j in range(i+1, len(fruits)):
            x1, y1 = fruits[i]
            x2, y2 = fruits[j]
            if x1 == x2:
                continue
            m = (y2-y1)/(x2-x1)
            b = y1 - m*x1
            slices.append((m, b))
    return slices

def get_intersection(slices, fruits):
    intersections = []
    for slice in slices:
        m, b = slice
        for fruit in fruits:
            x, y = fruit
            if m*x + b == y:
                intersections.append(fruit)
                break
    return intersections

def get_max_slices(fruits):
    slices = get_slices(fruits)
    intersections = get_intersection(slices, fruits)
    return len(set(intersections))

def main():
    n, fruits = get_input()
    print(get_max_slices(fruits))

if __name__ == '__main__':
    main()

