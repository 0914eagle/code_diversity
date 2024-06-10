
def get_min_length(start_times, speeds):
    # Find the maximum start time
    max_start_time = max(start_times)
    
    # Initialize the minimum length and the current length of the pack
    min_length = 0
    current_length = 0
    
    # Iterate over the start times and speeds
    for i in range(len(start_times)):
        # Calculate the distance traveled by the current cheetah
        distance = (start_times[i] / speeds[i])
        
        # If the current cheetah is the first to reach the finish line, update the minimum length
        if start_times[i] == max_start_time:
            min_length = current_length + distance
        
        # Update the current length of the pack
        current_length += distance
    
    return min_length

def main():
    # Read the number of cheetahs and their start times and speeds
    num_cheetahs = int(input())
    start_times = []
    speeds = []
    for i in range(num_cheetahs):
        start_times.append(int(input()))
        speeds.append(int(input()))
    
    # Calculate the minimum length of the pack
    min_length = get_min_length(start_times, speeds)
    
    # Print the minimum length of the pack
    print(min_length)

if __name__ == '__main__':
    main()

