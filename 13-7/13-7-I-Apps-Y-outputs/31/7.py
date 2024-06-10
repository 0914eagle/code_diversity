
def get_maximum_fraction(n, capacities, gas_canisters):
    # Sort the gas canisters in non-decreasing order
    sorted_gas_canisters = sorted(gas_canisters)

    # Initialize the minimum fraction to 0
    min_fraction = 0

    # Iterate through the balloons and gas canisters
    for i in range(n):
        # Calculate the capacity of the balloon
        capacity = capacities[i]

        # Calculate the amount of helium needed to fill the balloon to its capacity
        needed_helium = capacity - capacities[i]

        # If the needed helium is greater than the amount of helium in the current gas canister, return "impossible"
        if needed_helium > sorted_gas_canisters[i]:
            return "impossible"

        # Otherwise, calculate the fraction of the balloon that can be filled with helium
        fraction = needed_helium / capacity

        # Update the minimum fraction if the current fraction is less than the minimum fraction
        if fraction < min_fraction:
            min_fraction = fraction

    # Return the minimum fraction
    return min_fraction

def main():
    n = int(input())
    capacities = list(map(int, input().split()))
    gas_canisters = list(map(int, input().split()))
    print(get_maximum_fraction(n, capacities, gas_canisters))

if __name__ == '__main__':
    main()

