
import math

def get_min_pack_length(N, start_times, speeds):
    # Sort the cheetahs by their start times
    sorted_cheetahs = sorted(zip(start_times, speeds), key=lambda x: x[0])

    # Initialize the minimum pack length and the current position of the last cheetah
    min_pack_length = math.inf
    last_position = 0

    # Iterate over the cheetahs in order of their start times
    for i in range(N):
        # Get the current cheetah's start time and speed
        start_time, speed = sorted_cheetahs[i]

        # Calculate the distance the cheetah will travel before it reaches the finish line
        distance = speed * (start_time - last_position)

        # Update the minimum pack length if necessary
        min_pack_length = min(min_pack_length, distance)

        # Update the position of the last cheetah
        last_position = start_time + distance

    return min_pack_length

def main():
    N = int(input())
    start_times = []
    speeds = []
    for i in range(N):
        start_time, speed = map(int, input().split())
        start_times.append(start_time)
        speeds.append(speed)
    min_pack_length = get_min_pack_length(N, start_times, speeds)
    print(f"{min_pack_length:.3f}")

if __name__ == '__main__':
    main()

