
def get_maximum_fraction(n, capacities, canisters):
    # Sort the capacities in non-decreasing order
    sorted_capacities = sorted(capacities)

    # Initialize the minimum fraction to be 0
    minimum_fraction = 0

    # Loop through each canister
    for i in range(n):
        # Find the index of the smallest balloon that is not yet filled
        smallest_balloon_index = 0
        while smallest_balloon_index < n and capacities[smallest_balloon_index] <= 0:
            smallest_balloon_index += 1

        # If all balloons are filled, return the minimum fraction
        if smallest_balloon_index == n:
            return minimum_fraction

        # Fill the smallest balloon with the current canister
        capacities[smallest_balloon_index] -= canisters[i]

        # If the balloon is now filled beyond its capacity, return "impossible"
        if capacities[smallest_balloon_index] < 0:
            return "impossible"

        # Update the minimum fraction
        minimum_fraction = max(minimum_fraction, capacities[smallest_balloon_index] / sorted_capacities[smallest_balloon_index])

    # Return the minimum fraction
    return minimum_fraction

def main():
    n = int(input())
    capacities = list(map(int, input().split()))
    canisters = list(map(int, input().split()))
    print(get_maximum_fraction(n, capacities, canisters))

if __name__ == '__main__':
    main()

