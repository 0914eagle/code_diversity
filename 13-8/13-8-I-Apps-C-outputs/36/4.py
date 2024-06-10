
def get_min_length(start_times, speeds):
    # Sort the cheetahs by their start times
    sorted_cheetahs = sorted(zip(start_times, speeds), key=lambda x: x[0])

    # Initialize the minimum length and the current position of the first cheetah
    min_length = 0
    current_position = 0

    # Iterate through the sorted cheetahs
    for i in range(len(sorted_cheetahs)):
        # Get the current cheetah's start time and speed
        start_time, speed = sorted_cheetahs[i]

        # Calculate the current cheetah's position based on its start time and speed
        current_position += (start_time - current_position) * speed

        # Update the minimum length if the current position is greater than the previous minimum length
        min_length = max(min_length, current_position)

    return min_length

def main():
    # Read the number of cheetahs and their start times and speeds from stdin
    num_cheetahs = int(input())
    start_times = list(map(int, input().split()))
    speeds = list(map(int, input().split()))

    # Call the get_min_length function to get the minimum length of the running pack
    min_length = get_min_length(start_times, speeds)

    # Print the minimum length to stdout
    print(min_length)

if __name__ == '__main__':
    main()

