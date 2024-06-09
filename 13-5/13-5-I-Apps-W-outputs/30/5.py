
import math

def f1(W):
    # Calculate the distance between Agneta and Beata at time W
    distance = math.sqrt(2) - math.sin(W)
    return distance

def f2(W):
    # Calculate the minimum distance between Agneta and Beata during the ride
    min_distance = math.sqrt(2)
    for i in range(1001):
        distance = f1(i/1000)
        if distance < min_distance:
            min_distance = distance
    return min_distance

if __name__ == '__main__':
    W = float(input())
    print(f2(W))

