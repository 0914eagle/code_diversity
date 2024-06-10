
def get_safety_factor(lanes, cars, sensor_range):
    # Initialize the safety factor to 0
    safety_factor = 0
    
    # Iterate over each lane
    for lane in lanes:
        # Get the cars in the current lane
        lane_cars = [car for car in cars if car[0] == lane]
        
        # Sort the cars in the lane by their distance from the start of the sensor range
        lane_cars.sort(key=lambda x: x[2])
        
        # Iterate over the cars in the lane
        for i in range(len(lane_cars)):
            # Get the current car and its distance from the start of the sensor range
            car = lane_cars[i]
            distance = car[2]
            
            # Check if the car is within the sensor range
            if distance <= sensor_range:
                # Get the next car in the lane
                next_car = lane_cars[i+1] if i+1 < len(lane_cars) else None
                
                # Check if the next car is within the sensor range
                if next_car and next_car[2] <= sensor_range:
                    # Calculate the distance between the current car and the next car
                    distance_between_cars = next_car[2] - distance
                    
                    # Update the safety factor
                    safety_factor = max(safety_factor, distance_between_cars)
    
    return safety_factor

def main():
    # Read the input
    lanes, cars, sensor_range = map(int, input().split())
    cars = [list(map(int, input().split())) for _ in range(cars)]
    
    # Get the safety factor
    safety_factor = get_safety_factor(lanes, cars, sensor_range)
    
    # Print the safety factor
    print(safety_factor)

if __name__ == '__main__':
    main()

