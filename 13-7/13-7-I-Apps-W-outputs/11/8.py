
import math

def get_distance(W):
    # Agneta's vertical speed
    v1 = 1
    # Beata's vertical speed
    v2 = 2
    # Angular speed around the centre
    w = 1
    # Time difference between Agneta and Beata's descent
    t = W

    # Calculate the distance between Agneta and Beata at time t
    distance = (v1 * t + v2 * t + (v2 - v1) * w * t * t / 2) / (v1 + v2)

    return distance

def get_min_distance():
    # Minimum distance between Agneta and Beata
    min_distance = math.inf
    # Maximum time difference between Agneta and Beata's descent
    max_time = 1000

    # Iterate through all possible time differences between Agneta and Beata's descent
    for t in range(max_time + 1):
        # Calculate the distance between Agneta and Beata at time t
        distance = get_distance(t)
        # Update the minimum distance if necessary
        if distance < min_distance:
            min_distance = distance

    return min_distance

if __name__ == '__main__':
    W = float(input())
    print(get_min_distance())

