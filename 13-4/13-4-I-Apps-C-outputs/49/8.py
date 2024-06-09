
def get_min_cuts(poles, fence_length):
    # Sort the poles in descending order
    poles.sort(reverse=True)
    # Initialize variables to keep track of the cuts and the fence length
    cuts = 0
    fence_len = 0
    # Loop through the poles and check if they are long enough to be used as fence posts
    for pole in poles:
        if fence_len + pole <= fence_length:
            # If the pole is long enough, add it to the fence length and increment the cuts
            fence_len += pole
            cuts += 1
        else:
            # If the pole is not long enough, break the loop because the remaining poles will not be long enough
            break
    # Return the minimum number of cuts needed to build the fence
    return cuts

def main():
    # Read the input data
    K, N = map(int, input().split())
    poles = list(map(int, input().split()))
    # Call the function to get the minimum number of cuts
    cuts = get_min_cuts(poles, N)
    # Print the output
    print(cuts)

if __name__ == '__main__':
    main()

