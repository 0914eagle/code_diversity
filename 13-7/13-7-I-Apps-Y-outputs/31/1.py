
def get_maximum_fraction(balloons, gas_canisters):
    # Sort the gas canisters in descending order
    sorted_gas_canisters = sorted(gas_canisters, reverse=True)

    # Initialize the maximum fraction as 0
    maximum_fraction = 0

    # Loop through each balloon
    for balloon in balloons:
        # Find the largest gas canister that is less than or equal to the balloon's capacity
        largest_gas_canister = next((x for x in sorted_gas_canisters if x <= balloon), None)

        # If there is no gas canister that is large enough, return "impossible"
        if largest_gas_canister is None:
            return "impossible"

        # Calculate the fraction of the balloon that can be filled with helium
        fraction = largest_gas_canister / balloon

        # Update the maximum fraction if necessary
        maximum_fraction = max(maximum_fraction, fraction)

    # Return the maximum fraction
    return maximum_fraction

def main():
    balloons = [6, 1, 3, 2, 2, 3]
    gas_canisters = [6, 1, 3, 2, 2, 3]
    print(get_maximum_fraction(balloons, gas_canisters))

if __name__ == '__main__':
    main()

