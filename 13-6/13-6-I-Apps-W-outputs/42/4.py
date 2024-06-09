
def get_number_of_ways(n, k, lamps):
    # Initialize a list to store the answers for each subproblem
    dp = [0] * (k + 1)
    dp[0] = 1

    # Loop through each lamp
    for i in range(n):
        # Loop through each number of lamps to turn on
        for j in range(k, 0, -1):
            # If the current lamp's period is within the time period of the current combination of lamps
            if lamps[i][0] <= j and lamps[i][1] >= j:
                # Add the number of ways to turn on the current lamp to the answer for the current combination of lamps
                dp[j] = (dp[j] + dp[j - 1]) % 998244353

    # Return the answer for the total number of lamps to turn on
    return dp[k]

def main():
    n, k = map(int, input().split())
    lamps = []
    for i in range(n):
        l, r = map(int, input().split())
        lamps.append([l, r])
    print(get_number_of_ways(n, k, lamps))

if __name__ == '__main__':
    main()

