
def get_min_time(d, k, a, b, t):
    # Initialize variables
    time = 0
    distance = 0
    car_breaks = False

    # Loop through the distance
    while distance < d:
        # If the car is not broken, drive on the car
        if not car_breaks:
            time += a
            distance += k
        # If the car is broken, walk on foot
        else:
            time += b
            distance += 1

        # Check if the car needs to be repaired
        if distance % k == 0 and distance > 0:
            time += t
            car_breaks = True

    return time

def main():
    d, k, a, b, t = map(int, input().split())
    print(get_min_time(d, k, a, b, t))

if __name__ == '__main__':
    main()

