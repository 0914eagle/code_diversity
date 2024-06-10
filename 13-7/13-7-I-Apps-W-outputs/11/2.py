
import math

def calculate_distance(W):
    # Calculate the distance between Agneta and Beata at time W
    distance = 1 + W * 1
    return distance

def calculate_min_distance(W):
    # Calculate the minimum distance between Agneta and Beata during their trip
    min_distance = 1
    for i in range(1, 1000):
        distance = calculate_distance(i)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def main():
    W = float(input())
    print(calculate_min_distance(W))

if __name__ == '__main__':
    main()

