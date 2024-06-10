
def get_min_time(d, k, a, b, t):
    # Initialize variables
    time = 0
    distance = 0
    car_broken = False

    # Loop until the post office is reached
    while distance < d:
        # Calculate the distance that can be driven on the car
        drive_distance = min(k - distance, d - distance)

        # If the car is not broken, drive the calculated distance
        if not car_broken:
            time += drive_distance * a
            distance += drive_distance

        # If the car is broken, walk the calculated distance
        else:
            time += drive_distance * b
            distance += drive_distance

        # If the car is broken and the time to repair it has passed, repair the car
        if car_broken and time >= t:
            time += t
            car_broken = False

        # If the car is not broken and the distance to the post office has been reached, break the loop
        elif not car_broken and distance >= d:
            break

        # If the car is not broken and the distance to the post office has not been reached, break the loop
        elif not car_broken and distance < d:
            break

        # If the car is broken and the distance to the post office has been reached, break the loop
        elif car_broken and distance >= d:
            break

        # If the car is broken and the distance to the post office has not been reached, break the loop
        elif car_broken and distance < d:
            break

    return time

def main():
    d, k, a, b, t = map(int, input().split())
    print(get_min_time(d, k, a, b, t))

if __name__ == '__main__':
    main()

