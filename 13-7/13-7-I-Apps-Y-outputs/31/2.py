
def get_max_fraction(n, capacities, canisters):
    # Sort the canisters in non-increasing order
    sorted_canisters = sorted(canisters, reverse=True)

    # Initialize the fraction of helium in each balloon to 0
    fractions = [0] * n

    # Iterate through the canisters and assign them to the balloons
    for i, canister in enumerate(sorted_canisters):
        # Find the balloon with the smallest fraction of helium
        smallest_fraction_index = fractions.index(min(fractions))

        # Assign the canister to the balloon with the smallest fraction of helium
        fractions[smallest_fraction_index] += canister

        # If the balloon is now full, remove it from the list of fractions
        if fractions[smallest_fraction_index] >= capacities[smallest_fraction_index]:
            fractions.pop(smallest_fraction_index)

    # If all balloons have been filled, return the maximum fraction
    if not fractions:
        return max(fractions)
    else:
        return "impossible"

def main():
    n = int(input())
    capacities = list(map(int, input().split()))
    canisters = list(map(int, input().split()))
    print(get_max_fraction(n, capacities, canisters))

if __name__ == '__main__':
    main()

