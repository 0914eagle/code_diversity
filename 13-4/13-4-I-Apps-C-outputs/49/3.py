
def get_min_cuts(poles, fence_length):
    # Sort the poles in non-decreasing order
    poles.sort()
    # Initialize the minimum number of cuts to 0
    min_cuts = 0
    # Loop through the poles and find the longest one that is less than or equal to the fence length
    for pole in poles:
        if pole <= fence_length:
            # Add the length of the pole to the minimum number of cuts
            min_cuts += pole
            # Subtract the length of the pole from the fence length
            fence_length -= pole
        else:
            # If the pole is greater than the fence length, we need to make a cut
            min_cuts += 1
            # Subtract the fence length from the pole length
            pole -= fence_length
            # Add the fence length to the minimum number of cuts
            min_cuts += fence_length
            # Break out of the loop because we have found the longest pole that is less than or equal to the fence length
            break
    # Return the minimum number of cuts
    return min_cuts

def main():
    # Read the input data
    K, N = map(int, input().split())
    poles = list(map(int, input().split()))
    # Call the function to get the minimum number of cuts
    min_cuts = get_min_cuts(poles, N)
    # Print the minimum number of cuts
    print(min_cuts)

if __name__ == '__main__':
    main()

