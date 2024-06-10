
def get_sensor_readings(lanes, sensor_range):
    # Initialize a list to store the sensor readings for each lane
    sensor_readings = [[] for _ in range(lanes)]
    
    # Fill the sensor readings for each lane
    for i in range(lanes):
        for j in range(sensor_range):
            sensor_readings[i].append(j)
    
    return sensor_readings

def get_lane_switch_plan(lanes, sensor_readings, car_length, car_distance):
    # Initialize a list to store the lane switch plan
    lane_switch_plan = []
    
    # Fill the lane switch plan
    for i in range(lanes):
        # Check if the current lane is empty
        if len(sensor_readings[i]) == 0:
            # Add a "switch to this lane" command to the plan
            lane_switch_plan.append(i)
            break
        # Check if the current lane has enough space for the car
        elif sensor_readings[i][0] > car_length:
            # Add a "switch to this lane" command to the plan
            lane_switch_plan.append(i)
            break
        # Check if the current lane is the last lane
        elif i == lanes - 1:
            # Add an "impossible" command to the plan
            lane_switch_plan.append("Impossible")
            break
    
    return lane_switch_plan

def get_safety_factor(lanes, sensor_readings, car_length, car_distance):
    # Initialize a variable to store the safety factor
    safety_factor = 0
    
    # Fill the safety factor
    for i in range(lanes):
        # Check if the current lane is the destination lane
        if i == sensor_readings[0]:
            # Add the distance to the safety factor
            safety_factor += sensor_readings[i][0]
            break
        # Check if the current lane is the last lane
        elif i == lanes - 1:
            # Add the distance to the safety factor
            safety_factor += sensor_readings[i][0]
            break
    
    return safety_factor

def main():
    # Read the input
    lanes, cars, sensor_range = map(int, input().split())
    sensor_readings = get_sensor_readings(lanes, sensor_range)
    
    # Fill the sensor readings for each car
    for i in range(cars):
        lane, length, distance = map(int, input().split())
        sensor_readings[lane].append(distance)
    
    # Get the lane switch plan
    lane_switch_plan = get_lane_switch_plan(lanes, sensor_readings, length, distance)
    
    # Get the safety factor
    safety_factor = get_safety_factor(lanes, sensor_readings, length, distance)
    
    # Print the output
    if lane_switch_plan[0] == "Impossible":
        print("Impossible")
    else:
        print(safety_factor)

if __name__ == '__main__':
    main()

