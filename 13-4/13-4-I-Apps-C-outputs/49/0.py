
def get_min_cuts(poles, n):
    # Sort the poles in non-decreasing order
    poles.sort()
    # Initialize the minimum number of cuts to 0
    min_cuts = 0
    # Loop through the poles and calculate the minimum number of cuts needed
    for i in range(len(poles)):
        # Calculate the length of the current pole
        length = poles[i]
        # Calculate the number of cuts needed for the current pole
        cuts = (n - 1) // length
        # Add the number of cuts to the minimum number of cuts
        min_cuts += cuts
        # Subtract the length of the current pole from the total length of the fence
        n -= length
    # Return the minimum number of cuts
    return min_cuts

def main():
    # Read the number of poles and the length of the fence from stdin
    k, n = map(int, input().split())
    # Read the lengths of the poles from stdin
    poles = list(map(int, input().split()))
    # Call the get_min_cuts function and print the result
    print(get_min_cuts(poles, n))

if __name__ == '__main__':
    main()

