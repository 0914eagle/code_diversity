
def get_min_length(start_times, speeds):
    # Calculate the distance traveled by each cheetah
    distances = [speed * (max(start_times) - start_time) for start_time, speed in zip(start_times, speeds)]
    
    # Find the minimum distance traveled by all cheetahs
    min_distance = min(distances)
    
    # Return the minimum length of the running pack
    return min_distance

def main():
    # Read the number of cheetahs and their start times and speeds
    num_cheetahs = int(input())
    start_times = []
    speeds = []
    for _ in range(num_cheetahs):
        start_time, speed = map(int, input().split())
        start_times.append(start_time)
        speeds.append(speed)
    
    # Calculate the minimum length of the running pack
    min_length = get_min_length(start_times, speeds)
    
    # Print the minimum length of the running pack
    print(min_length)

if __name__ == '__main__':
    main()

