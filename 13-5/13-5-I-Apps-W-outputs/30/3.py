
import math

def calculate_distance(time):
    # Calculate the distance between Agneta and Beata at time t
    distance = math.sqrt(2) * math.sin(time)
    return distance

def calculate_min_distance(wait_time):
    # Calculate the minimum distance between Agneta and Beata over the entire ride
    min_distance = float('inf')
    for t in range(0, 1001):
        distance = calculate_distance(t)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def main():
    wait_time = float(input())
    min_distance = calculate_min_distance(wait_time)
    print(min_distance)

if __name__ == '__main__':
    main()

