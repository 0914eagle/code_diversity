
def get_min_pack_length(N, start_times, speeds):
    # Sort the cheetahs by their start times
    sorted_cheetahs = sorted(zip(start_times, speeds), key=lambda x: x[0])

    # Initialize the minimum pack length and the current position of the first cheetah
    min_pack_length = 0
    current_position = 0

    # Iterate through the cheetahs and calculate the minimum pack length
    for i in range(N):
        # Calculate the position of the current cheetah based on its speed and the time since it was released
        current_position += sorted_cheetahs[i][1] * (sorted_cheetahs[i][0] - current_time)

        # Update the minimum pack length if the current position is less than the previous minimum
        if current_position < min_pack_length:
            min_pack_length = current_position

    return min_pack_length

def main():
    N = int(input())
    start_times = []
    speeds = []
    for i in range(N):
        start_times.append(int(input()))
        speeds.append(int(input()))
    print(get_min_pack_length(N, start_times, speeds))

if __name__ == '__main__':
    main()

