
def get_min_length(start_times, velocities):
    # Sort the cheetahs by their start times
    sorted_cheetahs = sorted(zip(start_times, velocities), key=lambda x: x[0])

    # Initialize the minimum length and the current position of the first cheetah
    min_length = 0
    current_position = 0

    # Iterate through the sorted cheetahs
    for i in range(len(sorted_cheetahs)):
        # Get the current cheetah's start time and velocity
        start_time, velocity = sorted_cheetahs[i]

        # Update the current position of the first cheetah
        current_position += (start_time - current_position) * velocity

        # Update the minimum length
        min_length = max(min_length, current_position)

    return min_length

def main():
    # Read the number of cheetahs and their start times and velocities
    num_cheetahs = int(input())
    start_times = []
    velocities = []
    for _ in range(num_cheetahs):
        start_time, velocity = map(int, input().split())
        start_times.append(start_time)
        velocities.append(velocity)

    # Get the minimum length of the running pack
    min_length = get_min_length(start_times, velocities)

    # Print the minimum length
    print(f"{min_length:.3f}")

if __name__ == '__main__':
    main()

