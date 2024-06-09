
import math

def f1(W):
    # Calculate the distance between Agneta and Beata at time t
    def distance(t):
        Agneta_x = math.sin(t)
        Agneta_y = math.cos(t)
        Beata_x = math.sin(t + W)
        Beata_y = math.cos(t + W)
        return math.sqrt((Agneta_x - Beata_x)**2 + (Agneta_y - Beata_y)**2)

    # Find the minimum distance by calculating the distance at multiple points
    min_distance = float('inf')
    for t in range(0, 1001):
        distance_at_t = distance(t / 1000)
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
        return math.sqrt((Agneta_x - Beata_x)**2 + (Agneta_y - Beata_y)**2)

    # Find the minimum distance by calculating the distance at multiple points
    min_distance = float('inf')
    for t in range(0, 1001):
        distance_at_t = distance(t / 1000)
        if distance_at_t < min_distance:
            min_distance = distance_at_t

    return min_distance

if __name__ == '__main__':
    W = float(input())
    print(f1(W))
    print(f2(W))

