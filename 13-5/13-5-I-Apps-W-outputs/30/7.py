
import math

def get_distance(t):
    # Calculate the distance between Agneta and Beata at time t
    distance = 1 - math.cos(t)
    return distance

def get_min_distance(W):
    # Find the minimum distance between Agneta and Beata during their trip
    min_distance = float('inf')
    for t in range(0, 1001):
        distance = get_distance(t)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def main():
    W = float(input())
    print(get_min_distance(W))

if __name__ == '__main__':
    main()

