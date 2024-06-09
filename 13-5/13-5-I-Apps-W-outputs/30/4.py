
import math

def get_distance(t):
    # Calculate the distance between Agneta and Beata at time t
    distance = math.sqrt((1 - math.cos(t)) ** 2 + (math.sin(t)) ** 2)
    return distance

def get_min_distance(W):
    # Find the minimum distance between Agneta and Beata over the time period [0, W]
    min_distance = float('inf')
    for t in range(0, W + 1):
        distance = get_distance(t)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def main():
    W = float(input())
    print(get_min_distance(W))

if __name__ == '__main__':
    main()

