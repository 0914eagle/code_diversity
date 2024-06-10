
def get_safety_factor(lane_switch_plan):
    # Calculate the safety factor by taking the minimum distance to any car in the same lane
    safety_factor = min(lane_switch_plan, key=lambda x: x[1])[1]
    return safety_factor

def lane_switch_plan(lanes, cars, sensor_range):
    # Initialize the lane switch plan as a list of (lane, distance) tuples
    lane_switch_plan = [(0, 0)]

    # Loop through each car in the same lane as the ACM car
    for car in cars:
        # If the car is in the same lane as the ACM car and is within the sensor range
        if car[0] == 0 and car[2] <= sensor_range:
            # Add the car to the lane switch plan with its distance from the start of the sensor range
            lane_switch_plan.append((car[0], car[2]))

    # Sort the lane switch plan by distance from the start of the sensor range
    lane_switch_plan.sort(key=lambda x: x[1])

    # Return the lane switch plan with the highest safety factor
    return lane_switch_plan

def main():
    # Read the input data
    lanes, cars, sensor_range = map(int, input().split())
    cars = [tuple(map(int, input().split())) for _ in range(cars)]

    # Calculate the lane switch plan and the safety factor
    lane_switch_plan = lane_switch_plan(lanes, cars, sensor_range)
    safety_factor = get_safety_factor(lane_switch_plan)

    # Print the safety factor
    print(safety_factor)

if __name__ == '__main__':
    main()

