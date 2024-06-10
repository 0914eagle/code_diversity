
def get_time_to_reach_post_office(distance, car_distance, car_time, walking_time, repair_time):
    # Initialize variables
    time = 0
    distance_traveled = 0
    car_broken = False

    # Loop through the distance
    while distance_traveled < distance:
        # If the car is not broken, drive the car
        if not car_broken:
            # Calculate the distance that can be traveled by the car
            distance_traveled += min(distance - distance_traveled, car_distance)
            time += distance_traveled * car_time
            car_broken = True
        # If the car is broken, walk the remaining distance
        else:
            # Calculate the distance that needs to be walked
            distance_traveled += min(distance - distance_traveled, walking_time // car_time)
            time += distance_traveled * walking_time
            car_broken = False
            time += repair_time

    return time

def main():
    distance, car_distance, car_time, walking_time, repair_time = map(int, input().split())
    print(get_time_to_reach_post_office(distance, car_distance, car_time, walking_time, repair_time))

if __name__ == '__main__':
    main()

