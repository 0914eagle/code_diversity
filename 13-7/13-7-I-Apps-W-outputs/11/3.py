
import math

def distance(t):
    # Calculate the distance between Agneta and Beata at time t
    return math.sqrt(2) - math.cos(t)

def minimum_distance(W):
    # Find the minimum distance by finding the minimum of the distance function over the range [0, W]
    return min(distance(t) for t in range(0, W + 1))

def main():
    W = float(input())
    print(minimum_distance(W))

if __name__ == '__main__':
    main()

