
def get_lane_switch_plan(num_lanes, sensor_range, car_locations):
    # Initialize the plan as impossible
    plan = "Impossible"
    
    # Iterate over each lane
    for lane in range(num_lanes):
        # Calculate the distance to the back of the car in the current lane
        distance_to_back = sum(car_location[1] for car_location in car_locations if car_location[0] == lane)
        
        # If the distance to the back of the car is less than the sensor range, the lane is safe to switch to
        if distance_to_back <= sensor_range:
            # Calculate the safety factor for the current lane
            safety_factor = distance_to_back / sensor_range
            
            # If the safety factor is higher than the current plan, update the plan
            if safety_factor > plan:
                plan = safety_factor
    
    return plan

def main():
    num_lanes, num_cars, sensor_range = map(int, input().split())
    car_locations = []
    
    for _ in range(num_cars):
        lane, length, distance = map(int, input().split())
        car_locations.append((lane, length, distance))
    
    plan = get_lane_switch_plan(num_lanes, sensor_range, car_locations)
    print(plan)

if __name__ == '__main__':
    main()

