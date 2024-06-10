
def get_maximum_fraction(n, capacities, canisters):
    # Sort the capacities in non-decreasing order
    sorted_capacities = sorted(capacities)

    # Initialize the maximum fraction to be 0
    max_fraction = 0

    # Iterate over the capacities and canisters
    for capacity, canister in zip(sorted_capacities, canisters):
        # Calculate the fraction of the capacity that can be filled with the current canister
        fraction = canister / capacity

        # Update the maximum fraction if necessary
        if fraction > max_fraction:
            max_fraction = fraction

    # Return the maximum fraction
    return max_fraction

def main():
    n = int(input())
    capacities = list(map(int, input().split()))
    canisters = list(map(int, input().split()))
    print(get_maximum_fraction(n, capacities, canisters))

if __name__ == '__main__':
    main()

