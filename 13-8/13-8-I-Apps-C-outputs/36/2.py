
def get_min_length(start_times, speeds):
    # Calculate the time it takes for each cheetah to reach the finish line
    finish_times = [start_time + speed for start_time, speed in zip(start_times, speeds)]
    
    # Sort the cheetahs by their finish time in ascending order
    sorted_cheetahs = sorted(zip(finish_times, speeds), key=lambda x: x[0])
    
    # Initialize the minimum length of the pack as the distance between the first and last cheetah
    min_length = sorted_cheetahs[-1][0] - sorted_cheetahs[0][0]
    
    # Iterate through the sorted cheetahs and calculate the minimum length of the pack at each moment
    for i in range(len(sorted_cheetahs) - 1):
        current_length = sorted_cheetahs[i + 1][0] - sorted_cheetahs[i][0]
        if current_length < min_length:
            min_length = current_length
    
    return min_length

def main():
    num_cheetahs = int(input())
    start_times = []
    speeds = []
    for _ in range(num_cheetahs):
        start_time, speed = map(int, input().split())
        start_times.append(start_time)
        speeds.append(speed)
    print(get_min_length(start_times, speeds))

if __name__ == '__main__':
    main()

