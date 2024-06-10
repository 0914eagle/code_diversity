
def get_min_time(d, k, a, b, t):
    # Initialize variables
    time = 0
    distance = 0
    car_breaks = False

    # Loop until the destination is reached
    while distance < d:
        # Calculate the distance that can be covered by the car
        if car_breaks:
            car_distance = k - distance
        else:
            car_distance = d - distance

        # Calculate the time it takes to cover the distance by car or on foot
        if car_breaks:
            time += t + (car_distance * a)
        else:
            time += (car_distance * a)

        # Update the distance and car_breaks variables
        distance += car_distance
        car_breaks = not car_breaks

    # Return the final time
    return time

def main():
    d, k, a, b, t = map(int, input().split())
    print(get_min_time(d, k, a, b, t))

if __name__ == '__main__':
    main()

