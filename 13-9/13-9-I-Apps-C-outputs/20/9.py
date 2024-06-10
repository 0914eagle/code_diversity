
def get_pack_length(start_times, speeds):
    # Sort the cheetahs by their start time
    sorted_cheetahs = sorted(zip(start_times, speeds), key=lambda x: x[0])

    # Initialize the pack length and the previous cheetah's speed
    pack_length = 0
    prev_speed = 0

    # Iterate through the sorted cheetahs
    for start_time, speed in sorted_cheetahs:
        # Calculate the time difference between this cheetah and the previous one
        time_diff = start_time - prev_speed

        # Calculate the distance travelled by the previous cheetah during the time difference
        dist_travelled = prev_speed * time_diff

        # Update the pack length
        pack_length += dist_travelled

        # Update the previous cheetah's speed
        prev_speed = speed

    return pack_length

def main():
    # Read the input
    num_cheetahs = int(input())
    start_times = []
    speeds = []
    for _ in range(num_cheetahs):
        start_time, speed = map(int, input().split())
        start_times.append(start_time)
        speeds.append(speed)

    # Calculate the pack length
    pack_length = get_pack_length(start_times, speeds)

    # Print the output
    print(f"{pack_length:.3f}")

if __name__ == '__main__':
    main()

