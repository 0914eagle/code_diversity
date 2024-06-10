
import math

def calculate_distance(W):
    # Calculate the distance between Agneta and Beata at time W
    distance = math.sqrt((1 - math.cos(W)) / 2)
    return distance

def get_minimal_distance():
    # Find the minimal distance between Agneta and Beata during their trip
    minimal_distance = None
    for W in range(1001):
        distance = calculate_distance(W)
        if minimal_distance == None or distance < minimal_distance:
            minimal_distance = distance
    return minimal_distance

def main():
    W = float(input())
    print(get_minimal_distance())

if __name__ == '__main__':
    main()

