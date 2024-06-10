
def get_max_air_volume(tube_lengths, L1, L2):
    # Sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)
    
    # Initialize the maximum total length as 0
    max_total_length = 0
    
    # Loop through all possible pairs of tubes
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            # Check if the sum of the lengths of the first two tubes is less than or equal to L1
            if tube_lengths[i] + tube_lengths[j] <= L1:
                # Check if the sum of the lengths of the last two tubes is less than or equal to L2
                if tube_lengths[i+1] + tube_lengths[j+1] <= L2:
                    # Calculate the total length of the four tubes
                    total_length = tube_lengths[i] + tube_lengths[j] + tube_lengths[i+1] + tube_lengths[j+1]
                    # Update the maximum total length if necessary
                    if total_length > max_total_length:
                        max_total_length = total_length
    
    # Return the maximum total length or "Impossible" if no pair of tubes fits the constraints
    if max_total_length == 0:
        return "Impossible"
    else:
        return max_total_length

def main():
    L1, L2, N = map(int, input().split())
    tube_lengths = []
    for _ in range(N):
        tube_lengths.append(int(input()))
    print(get_max_air_volume(tube_lengths, L1, L2))

if __name__ == '__main__':
    main()

