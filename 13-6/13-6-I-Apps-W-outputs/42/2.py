
def get_number_of_ways(n, k, lamps):
    # Initialize a list to store the answers for each subproblem
    dp = [0] * (k + 1)
    dp[0] = 1

    # Loop through each lamp
    for i in range(n):
        # Loop through the number of lamps that can be turned on
        for j in range(k, 0, -1):
            # If the current lamp is turned on
            if lamps[i][0] <= j:
                # Add the number of ways to turn on j lamps to the answer
                dp[j] += dp[j - 1]

    # Return the answer modulo 998244353
    return dp[k] % 998244353

def main():
    n, k = map(int, input().split())
    lamps = []
    for i in range(n):
        l, r = map(int, input().split())
        lamps.append([l, r])
    print(get_number_of_ways(n, k, lamps))

if __name__ == '__main__':
    main()

