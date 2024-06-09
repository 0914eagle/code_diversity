
import math

def f1(n, m, s, t):
    # Initialize variables
    stations = [[] for _ in range(n)]
    for i in range(m):
        stations[i].append(i)
        stations[i].append(i+1)
    stations[m].append(m)
    stations[m].append(m+1)
    
    # Calculate the expected time to meet
    expected_time = 0
    current_station = s
    while current_station != t:
        expected_time += 1
        current_station = stations[current_station][0]
    
    return expected_time

def f2(n, m, s, t):
    # Initialize variables
    stations = [[] for _ in range(n)]
    for i in range(m):
        stations[i].append(i)
        stations[i].append(i+1)
    stations[m].append(m)
    stations[m].append(m+1)
    
    # Calculate the expected time to meet
    expected_time = 0
    current_station = s
    while current_station != t:
        expected_time += 1
        current_station = stations[current_station][0]
    
    return expected_time

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    s = int(input())
    t = int(input())
    print(f1(n, m, s, t))

