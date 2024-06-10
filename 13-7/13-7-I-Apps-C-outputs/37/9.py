
def get_tube_lengths(N):
    return [int(input()) for _ in range(N)]

def get_max_air_volume(tube_lengths, L1, L2):
    # Sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)
    # Initialize the total length of the tubes as 0
    total_length = 0
    # Initialize the number of tubes as 0
    num_tubes = 0
    # Iterate through the tube lengths
    for i in range(len(tube_lengths)):
        # Check if the total length of the tubes is less than L1
        if total_length < L1:
            # Add the current tube length to the total length
            total_length += tube_lengths[i]
            # Increment the number of tubes
            num_tubes += 1
        # Check if the total length of the tubes is greater than L1 and less than L2
        elif total_length < L2:
            # Add the current tube length to the total length
            total_length += tube_lengths[i]
            # Increment the number of tubes
            num_tubes += 1
            # Break out of the loop
            break
    # Check if the number of tubes is 4
    if num_tubes == 4:
        # Return the total length of the tubes
        return total_length
    else:
        # Return the string "Impossible"
        return "Impossible"

def main():
    # Read the inputs
    L1, L2, N = map(int, input().split())
    tube_lengths = get_tube_lengths(N)
    # Call the function to get the maximum air volume
    result = get_max_air_volume(tube_lengths, L1, L2)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

