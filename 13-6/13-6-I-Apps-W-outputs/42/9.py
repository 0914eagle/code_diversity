
def get_number_of_ways(n, k, lamps):
    # Initialize a dictionary to store the number of ways for each time
    number_of_ways = {0: 1}

    # Iterate over each lamp
    for i in range(n):
        # Get the period of time for the current lamp
        period = lamps[i][1] - lamps[i][0] + 1

        # Initialize a list to store the number of ways for each time in the current period
        ways = [0] * period

        # Iterate over each time in the current period
        for j in range(period):
            # Get the current time
            time = lamps[i][0] + j

            # If the current time is already in the dictionary, add the number of ways for the current lamp
            if time in number_of_ways:
                ways[j] += number_of_ways[time]

            # If the current time is not in the dictionary, but the previous time is, add the number of ways for the current lamp
            elif j > 0 and time - 1 in number_of_ways:
                ways[j] += number_of_ways[time - 1]

        # Add the number of ways for each time in the current period to the dictionary
        for j in range(period):
            number_of_ways[lamps[i][0] + j] = ways[j]

    # Return the number of ways for the desired time
    return number_of_ways[k] % 998244353

def main():
    n, k = map(int, input().split())
    lamps = []
    for i in range(n):
        l, r = map(int, input().split())
        lamps.append([l, r])
    print(get_number_of_ways(n, k, lamps))

if __name__ == '__main__':
    main()

