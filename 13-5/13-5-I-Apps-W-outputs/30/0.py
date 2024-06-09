
import math

def f1(W):
    # Calculate the distance between Agneta and Beata at time t
    def distance(t):
        Agneta_x = math.sin(t)
        Agneta_y = math.cos(t)
        Beata_x = math.sin(t + W)
        Beata_y = math.cos(t + W)
        return math.sqrt((Agneta_x - Beata_x) ** 2 + (Agneta_y - Beata_y) ** 2)

    # Find the minimum distance by iterating over all possible times t
    min_distance = float('inf')
    for t in range(0, 1000):
        distance_at_t = distance(t)
        if distance_at_t < min_distance:
            min_distance = distance_at_t

    return min_distance

def f2(W):
    # Calculate the distance between Agneta and Beata at time t
    def distance(t):
        Agneta_x = math.sin(t)
        Agneta_y = math.cos(t)
        Beata_x = math.sin(t + W)
        Beata_y = math.cos(t + W)
        return math.sqrt((Agneta_x - Beata_x) ** 2 + (Agneta_y - Beata_y) ** 2)

    # Find the minimum distance by using the derivative of the distance function
    min_distance = float('inf')
    for t in range(0, 1000):
        derivative = math.cos(t) - math.cos(t + W)
        if derivative == 0:
            continue
        distance_at_t = distance(t)
        min_distance = min(min_distance, distance_at_t)

    return min_distance

if __name__ == '__main__':
    W = float(input())
    print(f1(W))
    print(f2(W))

