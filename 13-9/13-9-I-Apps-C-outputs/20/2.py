
def get_min_pack_length(start_times, speeds):
    # Sort the cheetahs by their start times
    sorted_cheetahs = sorted(zip(start_times, speeds), key=lambda x: x[0])

    # Initialize the minimum length of the pack as the distance between the first and last cheetah
    min_length = sorted_cheetahs[-1][0] - sorted_cheetahs[0][0]

    # Iterate through the cheetahs and calculate the minimum length of the pack at each time
    for i in range(len(sorted_cheetahs) - 1):
        current_length = sorted_cheetahs[i + 1][0] - sorted_cheetahs[i][0]
        min_length = min(min_length, current_length)

    return min_length

def main():
    num_cheetahs = int(input())
    start_times = []
    speeds = []
    for i in range(num_cheetahs):
        start_time, speed = map(int, input().split())
        start_times.append(start_time)
        speeds.append(speed)
    print(get_min_pack_length(start_times, speeds))

if __name__ == '__main__':
    main()

