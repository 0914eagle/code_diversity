
def get_safest_lane_switch_plan(lanes, cars, sensor_range):
    # Initialize variables
    max_safety_factor = 0
    best_plan = []

    # Iterate over all possible lanes
    for lane in range(len(lanes)):
        # Calculate the safety factor for this lane
        safety_factor = calculate_safety_factor(lanes, cars, sensor_range, lane)

        # If this lane has the highest safety factor, update the best plan
        if safety_factor > max_safety_factor:
            max_safety_factor = safety_factor
            best_plan = [lane]

    # Return the best plan
    return best_plan

def calculate_safety_factor(lanes, cars, sensor_range, target_lane):
    # Initialize variables
    safety_factor = 0

    # Iterate over all cars in the target lane
    for car in lanes[target_lane]:
        # Calculate the distance between the car and the target lane
        distance = abs(car[1] - target_lane)

        # If the distance is within the sensor range, update the safety factor
        if distance <= sensor_range:
            safety_factor = max(safety_factor, distance)

    # Return the safety factor
    return safety_factor

def main():
    # Read the input
    num_lanes, num_cars, sensor_range = map(int, input().split())
    cars = []
    for _ in range(num_cars):
        lane, length, distance = map(int, input().split())
        cars.append([lane, length, distance])

    # Call the function to get the best plan
    plan = get_safest_lane_switch_plan(lanes, cars, sensor_range)

    # Print the output
    print(plan)

if __name__ == '__main__':
    main()

