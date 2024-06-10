
def get_safest_lane_switch(lanes, cars, sensor_range):
    # Initialize variables
    max_safety_factor = 0
    safest_lane = 0

    # Iterate over each lane
    for lane in range(len(lanes)):
        # Get the cars in the current lane
        lane_cars = [car for car in cars if car[0] == lane]

        # Sort the cars by their distance from the sensor range
        lane_cars.sort(key=lambda x: x[1])

        # Initialize variables for the current lane
        current_safety_factor = 0
        current_lane_distance = 0

        # Iterate over the cars in the current lane
        for car in lane_cars:
            # Calculate the distance from the sensor range to the back of the car
            car_distance = car[1] + car[2]

            # If the car is within the sensor range, calculate the safety factor
            if car_distance <= sensor_range:
                current_safety_factor += car_distance
                current_lane_distance += car[2]

        # If the current lane has a higher safety factor than the previous lanes, update the safest lane
        if current_safety_factor > max_safety_factor:
            max_safety_factor = current_safety_factor
            safest_lane = lane

    # Return the safest lane and safety factor
    return safest_lane, max_safety_factor

def get_lane_switch_plan(lanes, cars, sensor_range, current_lane):
    # Get the safest lane to switch to
    safest_lane, safety_factor = get_safest_lane_switch(lanes, cars, sensor_range)

    # If the safest lane is not the current lane, return a plan to switch to the safest lane
    if safest_lane != current_lane:
        return [safest_lane]

    # If the safest lane is the current lane, return an impossible plan
    return []

if __name__ == '__main__':
    # Get the input
    lanes, cars, sensor_range = map(int, input().split())
    cars = [list(map(int, input().split())) for _ in range(cars)]

    # Get the current lane of the ACM car
    current_lane = cars[0][0]

    # Get the lane switch plan
    plan = get_lane_switch_plan(lanes, cars, sensor_range, current_lane)

    # Print the plan
    print(plan)

