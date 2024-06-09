
import math

def solve(A, B):
    # Calculate the sum of distances between each pair of numbers in the interval [A, B]
    total_distance = 0
    for i in range(A, B+1):
        for j in range(A, B+1):
            total_distance += distance(i, j)
    
    # Return the result modulo 1000000007
    return total_distance % 1000000007

def distance(a, b):
    # Calculate the distance between a and b
    distance = 0
    for i in range(max(len(str(a)), len(str(b)))):
        x = int(str(a)[i]) if i < len(str(a)) else 0
        y = int(str(b)[i]) if i < len(str(b)) else 0
        distance += abs(x - y)
    return distance

