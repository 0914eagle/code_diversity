
def get_sensor_range(N, R):
    return list(range(N+1))

def get_lane_switch_plan(lane_num, sensor_range, car_length, car_dist):
    # Initialize the safety factor as the minimum possible value
    safety_factor = -1
    # Iterate over the lanes within the sensor range
    for i in range(lane_num+1, sensor_range+1):
        # Calculate the distance to the back of the car in the current lane
        dist_back = car_length - car_dist
        # Check if the current lane is unoccupied and has enough space for the car to move into
        if dist_back >= 0 and dist_back <= sensor_range:
            # Calculate the safety factor for the current lane
            safety_factor = max(safety_factor, dist_back)
    return safety_factor

def main():
    N, M, R = map(int, input().split())
    sensor_range = get_sensor_range(N, R)
    for i in range(M):
        lane_num, car_length, car_dist = map(int, input().split())
        safety_factor = get_lane_switch_plan(lane_num, sensor_range, car_length, car_dist)
        if safety_factor == -1:
            print("Impossible")
        else:
            print(safety_factor)

if __name__ == '__main__':
    main()

