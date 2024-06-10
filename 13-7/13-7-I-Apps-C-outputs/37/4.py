
def get_tube_lengths(N):
    # Read the N tube lengths from stdin
    tube_lengths = [int(input()) for _ in range(N)]
    return tube_lengths

def get_maximum_air_replacement(tube_lengths, L1, L2):
    # Sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)
    
    # Initialize the maximum air replacement to 0
    max_air_replacement = 0
    
    # Iterate over the tube lengths
    for i in range(len(tube_lengths)):
        # Check if the sum of the first two tube lengths is less than or equal to L1
        if sum(tube_lengths[:2]) <= L1:
            # Check if the sum of the last two tube lengths is less than or equal to L2
            if sum(tube_lengths[-2:]) <= L2:
                # Calculate the total length of the four tubes
                total_length = sum(tube_lengths[:4])
                
                # Update the maximum air replacement if the current total length is greater than the previous maximum
                if total_length > max_air_replacement:
                    max_air_replacement = total_length
    
    # Return the maximum air replacement
    return max_air_replacement

def main():
    # Read the input from stdin
    L1, L2, N = map(int, input().split())
    tube_lengths = get_tube_lengths(N)
    
    # Call the function to get the maximum air replacement
    max_air_replacement = get_maximum_air_replacement(tube_lengths, L1, L2)
    
    # Print the output
    if max_air_replacement == 0:
        print("Impossible")
    else:
        print(max_air_replacement)

if __name__ == '__main__':
    main()

