
import math

def f1(n, m, s, t):
    # Initialize variables
    stations = set([s, t])
    neighbors = set()
    for i in range(m):
        neighbors.add(tuple(map(int, input().split())))
    
    # Find the shortest path between the initial stations
    path = []
    current = s
    while current != t:
        for neighbor in neighbors:
            if current in neighbor and neighbor[0] != current and neighbor[1] not in path:
                path.append(neighbor[1])
                current = neighbor[1]
                break
    
    # Calculate the expected time to meet
    time = 0
    for i in range(len(path)):
        time += 1 / math.factorial(i + 1)
    
    return time

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    s = int(input())
    t = int(input())
    print(f1(n, m, s, t))

