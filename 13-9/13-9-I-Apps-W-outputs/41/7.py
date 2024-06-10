
import math

def get_speedometer_reading(distance, speedometer_reading):
    
    return distance / speedometer_reading

def get_journey_time(n, distance, speedometer_reading):
    
    journey_time = 0
    for i in range(n):
        segment_time = distance[i] / speedometer_reading[i]
        journey_time += segment_time
    return journey_time

def get_constant(n, distance, speedometer_reading, journey_time):
    
    # Calculate the average speed over the journey
    average_speed = sum(speedometer_reading) / n
    # Calculate the average speed over the journey with the constant applied
    average_speed_with_constant = sum(speedometer_reading) / (n - 1)
    # Calculate the constant by subtracting the average speed with the constant from the average speed without the constant
    constant = average_speed_with_constant - average_speed
    return constant

def main():
    n, t = map(int, input().split())
    distance = []
    speedometer_reading = []
    for _ in range(n):
        distance.append(int(input()))
        speedometer_reading.append(int(input()))
    journey_time = get_journey_time(n, distance, speedometer_reading)
    constant = get_constant(n, distance, speedometer_reading, journey_time)
    print(constant)

if __name__ == '__main__':
    main()

