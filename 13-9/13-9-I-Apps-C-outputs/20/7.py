
def get_min_pack_length(start_times, speeds):
    # Calculate the time it takes for each cheetah to reach the finish line
    finish_times = [start_time + speed for start_time, speed in zip(start_times, speeds)]
    
    # Sort the cheetahs by their finish time
    sorted_cheetahs = sorted(zip(finish_times, speeds), key=lambda x: x[0])
    
    # Initialize the minimum pack length and the current pack length
    min_pack_length = 0
    current_pack_length = 0
    
    # Iterate through the sorted cheetahs
    for finish_time, speed in sorted_cheetahs:
        # If the current pack length is 0, set it to the speed of the current cheetah
        if current_pack_length == 0:
            current_pack_length = speed
        # If the current pack length is not 0, add the speed of the current cheetah to the current pack length
        else:
            current_pack_length += speed
        
        # Update the minimum pack length if necessary
        min_pack_length = max(min_pack_length, current_pack_length)
    
    return min_pack_length

def main():
    num_cheetahs = int(input())
    start_times = []
    speeds = []
    
    for _ in range(num_cheetahs):
        start_time, speed = map(int, input().split())
        start_times.append(start_time)
        speeds.append(speed)
    
    print(get_min_pack_length(start_times, speeds))

if __name__ == '__main__':
    main()

