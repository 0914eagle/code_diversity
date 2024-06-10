
def get_time_to_reach_post_office(d, k, a, b, t):
    # Initialize variables
    time = 0
    distance = 0
    car_broken = False

    # Loop through the distance
    while distance < d:
        # If the car is broken, Vasiliy needs to walk
        if car_broken:
            time += b
            distance += 1
        # If the car is not broken, Vasiliy can drive
        else:
            time += a
            distance += 1

        # Check if the car needs to be repaired
        if distance % k == 0:
            time += t
            car_broken = True

    return time

def main():
    d, k, a, b, t = map(int, input().split())
    print(get_time_to_reach_post_office(d, k, a, b, t))

if __name__ == '__main__':
    main()

