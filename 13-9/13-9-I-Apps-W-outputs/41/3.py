
def get_speedometer_readings(n, t, dist_list, speed_list):
    # Calculate the time taken for each segment
    time_taken_list = [t/n for _ in range(n)]
    
    # Calculate the average speed for each segment
    avg_speed_list = [dist/time for dist, time in zip(dist_list, time_taken_list)]
    
    # Calculate the average speed for the entire journey
    avg_speed = sum(avg_speed_list) / n
    
    # Calculate the constant c
    c = avg_speed - sum(speed_list) / n
    
    return c

def main():
    n, t = map(int, input().split())
    dist_list = []
    speed_list = []
    for _ in range(n):
        dist, speed = map(int, input().split())
        dist_list.append(dist)
        speed_list.append(speed)
    c = get_speedometer_readings(n, t, dist_list, speed_list)
    print(round(c, 9))

if __name__ == '__main__':
    main()

