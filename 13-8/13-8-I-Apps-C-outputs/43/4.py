
import math

def get_safety_factor(lanes, cars, sensor_range):
    # Initialize the safety factor as infinity
    safety_factor = math.inf
    
    # Loop through each lane
    for lane in range(len(lanes)):
        # Get the cars in the current lane
        cars_in_lane = [car for car in cars if car[0] == lane]
        
        # Sort the cars in the current lane by their distance from the start of the sensor range
        cars_in_lane.sort(key=lambda x: x[1])
        
        # Loop through each car in the current lane
        for i in range(len(cars_in_lane)):
            # Get the current car's distance from the start of the sensor range
            current_distance = cars_in_lane[i][1]
            
            # Check if the current car's distance is within the sensor range
            if current_distance <= sensor_range:
                # Get the next car's distance from the start of the sensor range
                next_distance = cars_in_lane[i+1][1] if i < len(cars_in_lane) - 1 else sensor_range
                
                # Calculate the safety factor for the current car
                safety_factor = min(safety_factor, (next_distance - current_distance) / 2)
    
    return safety_factor

def solve(lanes, cars, sensor_range):
    # Get the safety factor for each lane
    safety_factors = [get_safety_factor(lane, cars, sensor_range) for lane in lanes]
    
    # Find the maximum safety factor
    max_safety_factor = max(safety_factors)
    
    # Check if the maximum safety factor is less than the sensor range
    if max_safety_factor < sensor_range:
        return "Impossible"
    else:
        return max_safety_factor

def main():
    lanes = int(input())
    cars = []
    sensor_range = int(input())
    
    for _ in range(lanes):
        cars.append([int(x) for x in input().split()])
    
    print(solve(lanes, cars, sensor_range))

if __name__ == '__main__':
    main()

