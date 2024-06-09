
import math

def solve(path):
    N = int(input())
    x_coords = [int(x) for x in input().split()]
    y_coords = [int(y) for y in input().split()]

    total_distance = 0
    for i in range(N):
        for j in range(i+1, N):
            total_distance += math.sqrt((x_coords[i] - x_coords[j])**2 + (y_coords[i] - y_coords[j])**2)

    return total_distance / math.factorial(N)

