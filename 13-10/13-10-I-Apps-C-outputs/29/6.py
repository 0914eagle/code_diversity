
import math
import sys

class Hill:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h
        self.spring = None
        self.town = None
        self.aqueduct = None

class Spring:
    def __init__(self, hill):
        self.hill = hill
        self.connected = False

    def get_flow(self):
        return self.hill.h

class Aqueduct:
    def __init__(self, length):
        self.length = length
        self.flow = 0

def read_input():
    global n, s, t, q, hills, springs, towns
    n, s, t, q = map(int, input().split())
    hills = []
    for i in range(n):
        x, y, h = map(int, input().split())
        hills.append(Hill(x, y, h))
    springs = []
    for i in range(s):
        springs.append(Spring(hills[int(input()) - 1]))
    towns = []
    for i in range(t):
        towns.append(hills[int(input()) - 1])

def calculate_flow():
    for spring in springs:
        flow = spring.get_flow()
        spring.connected = True
        for aqueduct in spring.hill.aqueducts:
            aqueduct.flow += flow

def find_path(town):
    for hill in hills:
        if hill.x == town.x and hill.y == town.y:
            return hill
    return None

def calculate_distance(start, end):
    return math.sqrt((start.x - end.x) ** 2 + (start.y - end.y) ** 2)

def connect_towns():
    for town in towns:
        path = find_path(town)
        while path:
            if path.spring:
                path.spring.connected = True
                break
            path = find_path(path)

def calculate_total_length():
    total_length = 0
    for spring in springs:
        if not spring.connected:
            continue
        for aqueduct in spring.hill.aqueducts:
            if not aqueduct.flow:
                continue
            total_length += aqueduct.length
    return total_length

def main():
    read_input()
    calculate_flow()
    connect_towns()
    total_length = calculate_total_length()
    print(total_length)

if __name__ == '__main__':
    main()

