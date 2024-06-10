
import math

def get_distance(t):
    # Calculate the distance between Agneta and Beata at time t
    x_agneta = math.sin(t)
    y_agneta = math.cos(t)
    x_beata = math.sin(t + 1)
    y_beata = math.cos(t + 1)
    distance = math.sqrt((x_agneta - x_beata)**2 + (y_agneta - y_beata)**2)
    return distance

def find_min_distance(W):
    # Find the minimum distance between Agneta and Beata over the time interval [0, W]
    min_distance = float('inf')
    for t in range(0, W):
        distance = get_distance(t)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def main():
    W = float(input())
    print(find_min_distance(W))

if __name__ == '__main__':
    main()

