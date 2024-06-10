
import math

def get_input():
    N = int(input())
    times = []
    speeds = []
    for i in range(N):
        time, speed = map(int, input().split())
        times.append(time)
        speeds.append(speed)
    return N, times, speeds

def get_min_pack_length(N, times, speeds):
    # Sort the cheetahs by their start time
    sorted_cheetahs = sorted(zip(times, speeds), key=lambda x: x[0])

    # Initialize the minimum pack length
    min_pack_length = float('inf')

    # Iterate through the cheetahs and calculate the minimum pack length
    for i in range(N):
        # Calculate the time it takes for the current cheetah to reach the finish line
        time_to_finish = (N - i) / speeds[i]

        # Calculate the minimum pack length for the current cheetah
        min_pack_length_curr = (time_to_finish + times[i]) * speeds[i]

        # Update the minimum pack length if necessary
        if min_pack_length_curr < min_pack_length:
            min_pack_length = min_pack_length_curr

    return min_pack_length

def main():
    N, times, speeds = get_input()
    min_pack_length = get_min_pack_length(N, times, speeds)
    print(min_pack_length)

if __name__ == '__main__':
    main()

