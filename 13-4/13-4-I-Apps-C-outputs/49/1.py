
def get_min_cuts(poles, n):
    # Sort the poles in non-decreasing order
    poles.sort()
    # Initialize the minimum number of cuts to 0
    min_cuts = 0
    # Loop through the poles and count the number of cuts needed
    for i in range(len(poles)):
        # Check if the current pole is longer than the desired length
        if poles[i] > n:
            # Calculate the number of cuts needed for the current pole
            cuts = (poles[i] - n) + 1
            # Update the minimum number of cuts
            min_cuts += cuts
    return min_cuts

def main():
    k, n = map(int, input().split())
    poles = list(map(int, input().split()))
    print(get_min_cuts(poles, n))

if __name__ == '__main__':
    main()

