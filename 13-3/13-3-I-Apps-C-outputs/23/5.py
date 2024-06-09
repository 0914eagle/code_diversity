
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
            if current in neighbor:
                path.append(neighbor)
                current = neighbor[0] if neighbor[0] != current else neighbor[1]
                break
    
    # Calculate the expected time to meet
    time = 0
    for i in range(len(path) - 1):
        time += 1
        stations.add(path[i + 1])
        for neighbor in neighbors:
            if path[i] in neighbor and path[i + 1] not in stations:
                time += 1
                break
    
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

