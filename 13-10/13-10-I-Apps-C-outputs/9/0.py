
def get_max_length(tubes, L1, L2):
    # Sort the tubes in descending order
    tubes.sort(reverse=True)
    # Initialize the maximum length and the pairs of tubes
    max_length = 0
    pairs = []
    # Iterate over the tubes
    for i in range(len(tubes)):
        # Check if the sum of the first two tubes is less than or equal to L1
        if tubes[i] + tubes[i+1] <= L1:
            # Check if the sum of the last two tubes is less than or equal to L2
            if tubes[i+2] + tubes[i+3] <= L2:
                # Calculate the total length of the four tubes
                total_length = tubes[i] + tubes[i+1] + tubes[i+2] + tubes[i+3]
                # Check if the total length is greater than the current maximum length
                if total_length > max_length:
                    # Update the maximum length and the pairs of tubes
                    max_length = total_length
                    pairs = [(tubes[i], tubes[i+1]), (tubes[i+2], tubes[i+3])]
    # Return the maximum length and the pairs of tubes
    return max_length, pairs

def main():
    # Read the input
    L1, L2, N = map(int, input().split())
    tubes = [int(input()) for _ in range(N)]
    # Call the get_max_length function
    max_length, pairs = get_max_length(tubes, L1, L2)
    # Check if there are no pairs of tubes fitting into the setup
    if max_length == 0:
        print("Impossible")
    else:
        # Print the maximum length and the pairs of tubes
        print(max_length)
        for pair in pairs:
            print(pair[0], pair[1])

if __name__ == '__main__':
    main()

