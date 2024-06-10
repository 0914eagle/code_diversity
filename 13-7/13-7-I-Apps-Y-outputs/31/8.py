
def get_maximum_fraction(n, capacities, gas_canisters):
    # Sort the gas canisters in non-decreasing order
    gas_canisters.sort()
    
    # Initialize the maximum fraction to 0
    max_fraction = 0
    
    # Iterate through the balloons and gas canisters
    for i in range(n):
        # Calculate the fraction of helium that can be placed in the balloon
        fraction = gas_canisters[i] / capacities[i]
        
        # Update the maximum fraction if necessary
        if fraction > max_fraction:
            max_fraction = fraction
    
    # Return the maximum fraction
    return max_fraction

def main():
    n = int(input())
    capacities = list(map(int, input().split()))
    gas_canisters = list(map(int, input().split()))
    print(get_maximum_fraction(n, capacities, gas_canisters))

if __name__ == '__main__':
    main()

