
def get_min_time(d, k, a, b, t):
    # Initialize variables
    time = 0
    distance = 0
    car_broken = False

    # Loop through each kilometer
    while distance < d:
        # If car is not broken, drive one kilometer on the car
        if not car_broken:
            time += a
            distance += 1
        # If car is broken, walk one kilometer on foot
        else:
            time += b
            distance += 1
        # If distance is a multiple of k, repair the car
        if distance % k == 0:
            time += t
            car_broken = False
        # If distance is not a multiple of k, break the car
        else:
            car_broken = True

    return time

def main():
    d, k, a, b, t = map(int, input().split())
    print(get_min_time(d, k, a, b, t))

if __name__ == '__main__':
    main()

