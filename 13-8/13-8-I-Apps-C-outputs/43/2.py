
def get_sensor_readings(lanes, sensor_range):
    # Initialize an empty list to store the sensor readings
    sensor_readings = []
    
    # Iterate over the lanes
    for lane in lanes:
        # Initialize an empty list to store the distances for each lane
        distances = []
        
        # Iterate over the cars in the lane
        for car in lane:
            # Calculate the distance between the car and the sensor range
            distance = car[1] - sensor_range
            
            # If the distance is negative, set it to 0
            if distance < 0:
                distance = 0
            
            # Add the distance to the list of distances for the lane
            distances.append(distance)
        
        # Add the list of distances for the lane to the list of sensor readings
        sensor_readings.append(distances)
    
    # Return the list of sensor readings
    return sensor_readings

def get_lane_switch_plan(sensor_readings, lanes, destination_lane):
    # Initialize the maximum safety factor to 0
    max_safety_factor = 0
    
    # Iterate over the lanes
    for lane in lanes:
        # Initialize the current safety factor to 0
        current_safety_factor = 0
        
        # Iterate over the cars in the lane
        for car in lane:
            # Calculate the distance between the car and the sensor range
            distance = car[1] - sensor_range
            
            # If the distance is negative, set it to 0
            if distance < 0:
                distance = 0
            
            # Add the distance to the current safety factor
            current_safety_factor += distance
        
        # If the current safety factor is greater than the maximum safety factor, set the maximum safety factor to the current safety factor
        if current_safety_factor > max_safety_factor:
            max_safety_factor = current_safety_factor
    
    # Return the maximum safety factor
    return max_safety_factor

def main():
    # Read the input
    N, M, R = map(int, input().split())
    lanes = []
    for i in range(N):
        lanes.append([])
    for i in range(M):
        lane, length, distance = map(int, input().split())
        lanes[lane].append((length, distance))
    
    # Get the sensor readings
    sensor_readings = get_sensor_readings(lanes, R)
    
    # Get the lane switch plan
    destination_lane = N - 1
    lane_switch_plan = get_lane_switch_plan(sensor_readings, lanes, destination_lane)
    
    # Print the lane switch plan
    print(lane_switch_plan)

if __name__ == '__main__':
    main()

