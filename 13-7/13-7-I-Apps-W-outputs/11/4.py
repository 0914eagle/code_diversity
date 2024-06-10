
import math

def distance(t):
    # Calculate the distance between Agneta and Beata at time t
    agneta_x = math.cos(t)
    agneta_y = math.sin(t)
    beata_x = math.cos(t + math.pi)
    beata_y = math.sin(t + math.pi)
    return math.sqrt((agneta_x - beata_x)**2 + (agneta_y - beata_y)**2)

def find_min_distance():
    # Find the minimum distance between Agneta and Beata over the entire ride
    min_distance = math.inf
    for t in range(1001):
        distance_at_time_t = distance(t)
        if distance_at_time_t < min_distance:
            min_distance = distance_at_time_t
    return min_distance

def main():
    # Read input and call function to find minimum distance
    wait_time = float(input())
    min_distance = find_min_distance()
    print(min_distance)

if __name__ == '__main__':
    main()

