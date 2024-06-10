
def get_min_time(d, k, a, b, t):
    # Initialize variables
    time = 0
    distance = 0
    car_broken = False

    # Loop through the distance
    while distance < d:
        # Calculate the distance that can be traveled by the car
        car_distance = min(d - distance, k - distance % k)

        # If the car is not broken, travel by car
        if not car_broken:
            time += car_distance * a
            distance += car_distance

        # If the car is broken, travel by foot
        else:
            time += car_distance * b
            distance += car_distance

        # Check if the car is broken and needs to be repaired
        if distance % k == 0:
            car_broken = True
            time += t

    return time

def main():
    d, k, a, b, t = map(int, input().split())
    print(get_min_time(d, k, a, b, t))

if __name__ == '__main__':
    main()

