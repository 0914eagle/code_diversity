
def get_min_time(a, b, taxi_positions):
    # Calculate the distance between Vasiliy's home and each taxi position
    distances = []
    for taxi_position in taxi_positions:
        distance = abs(taxi_position[0] - a) + abs(taxi_position[1] - b)
        distances.append(distance)
    
    # Return the minimum time it will take for Vasiliy to get in any of the Beru-taxi cars
    return min(distances) / max(taxi_positions, key=lambda x: x[2])[2]

def main():
    a, b = map(int, input().split())
    n = int(input())
    taxi_positions = []
    for _ in range(n):
        x, y, v = map(int, input().split())
        taxi_positions.append((x, y, v))
    print(get_min_time(a, b, taxi_positions))

if __name__ == '__main__':
    main()

