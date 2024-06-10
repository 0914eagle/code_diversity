
def get_min_length(start_times, speeds):
    # Calculate the time it takes for each cheetah to reach the finish line
    finish_times = [start_time + speed for start_time, speed in zip(start_times, speeds)]
    
    # Sort the cheetahs by their finish time
    sorted_cheetahs = sorted(enumerate(finish_times), key=lambda x: x[1])
    
    # Initialize the minimum length of the pack
    min_length = 0
    
    # Iterate over the cheetahs in order of their finish time
    for i, (cheetah_id, finish_time) in enumerate(sorted_cheetahs):
        # Calculate the length of the pack up to this point
        pack_length = finish_time - start_times[cheetah_id]
        
        # Update the minimum length of the pack if necessary
        if pack_length > min_length:
            min_length = pack_length
    
    return min_length

def main():
    num_cheetahs = int(input())
    start_times = []
    speeds = []
    for _ in range(num_cheetahs):
        start_time, speed = map(int, input().split())
        start_times.append(start_time)
        speeds.append(speed)
    min_length = get_min_length(start_times, speeds)
    print(min_length)

if __name__ == '__main__':
    main()

