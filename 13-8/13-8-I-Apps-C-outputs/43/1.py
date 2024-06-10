
import math

def get_safety_factor(lanes, sensor_range, cars):
    # Initialize the safety factor to 0
    safety_factor = 0
    
    # Iterate over each lane
    for lane in range(len(lanes)):
        # Get the length of the current lane
        lane_length = lanes[lane]
        
        # Iterate over each car in the current lane
        for car in cars[lane]:
            # Get the distance of the car from the start of the sensor range
            distance = car[1]
            
            # Check if the car is within the sensor range
            if distance <= sensor_range:
                # Calculate the safety factor for the current car
                sf = math.ceil(lane_length - distance)
                
                # Update the safety factor if it's higher than the current value
                safety_factor = max(safety_factor, sf)
    
    return safety_factor

def main():
    # Read the input
    lanes, cars, sensor_range = read_input()
    
    # Calculate the safety factor
    safety_factor = get_safety_factor(lanes, sensor_range, cars)
    
    # Print the output
    print(safety_factor)

def read_input():
    # Read the number of lanes, cars, and sensor range
    lanes, cars, sensor_range = map(int, input().split())
    
    # Initialize the cars list
    cars = [[] for _ in range(lanes)]
    
    # Read the cars information
    for _ in range(cars):
        lane, length, distance = map(int, input().split())
        cars[lane].append([length, distance])
    
    return lanes, cars, sensor_range

if __name__ == '__main__':
    main()

