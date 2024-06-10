
import math

def get_min_time(a, b, n, cars):
    # Calculate the distance between Vasiliy's home and each taxi location
    dist_to_cars = []
    for car in cars:
        dist_to_cars.append(math.sqrt((a - car[0])**2 + (b - car[1])**2))
    
    # Calculate the time it takes for each taxi to arrive at Vasiliy's home
    time_to_arrive = []
    for i in range(n):
        time_to_arrive.append(dist_to_cars[i] / cars[i][2])
    
    # Return the minimum time it takes for any taxi to arrive
    return min(time_to_arrive)

def main():
    a, b = map(int, input().split())
    n = int(input())
    cars = []
    for i in range(n):
        x, y, v = map(int, input().split())
        cars.append([x, y, v])
    print(get_min_time(a, b, n, cars))

if __name__ == '__main__':
    main()

