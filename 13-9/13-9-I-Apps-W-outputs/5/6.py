
def get_lamps(n, k, lamps):
    # Initialize a dictionary to store the number of ways to choose k lamps
    ways = {0: 1}
    
    # Iterate over the lamps
    for i in range(n):
        # Check if the current lamp is turned on
        if lamps[i]:
            # Iterate over the previous k lamps
            for j in range(k):
                # Check if the current lamp is turned on and the previous lamp is not turned on
                if lamps[i] and not lamps[j]:
                    # Increment the number of ways to choose k lamps
                    ways[i] = (ways[i] + ways[j]) % 998244353
    
    # Return the number of ways to choose k lamps
    return ways[n-1]

def main():
    # Read the input
    n, k = map(int, input().split())
    lamps = [False] * n
    for i in range(n):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            lamps[j-1] = True
    
    # Calculate the number of ways to choose k lamps
    ways = get_lamps(n, k, lamps)
    
    # Print the result
    print(ways)

if __name__ == '__main__':
    main()

