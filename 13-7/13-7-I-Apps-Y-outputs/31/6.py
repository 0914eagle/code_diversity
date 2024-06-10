
def get_balloon_sizes(n):
    return [i for i in range(1, n+1)]

def get_gas_canisters(n):
    return [i for i in range(n)]

def get_gas_canister_amounts(n):
    return [i for i in range(n)]

def assign_gas_canisters(balloon_sizes, gas_canisters, gas_canister_amounts):
    assigned_gas_canisters = []
    for balloon_size in balloon_sizes:
        gas_canister_index = gas_canisters.index(min(gas_canisters))
        assigned_gas_canisters.append(gas_canister_index)
        gas_canisters[gas_canister_index] -= balloon_size
    return assigned_gas_canisters

def get_balloon_fractions(balloon_sizes, assigned_gas_canisters, gas_canister_amounts):
    balloon_fractions = []
    for i in range(len(balloon_sizes)):
        balloon_fraction = gas_canister_amounts[assigned_gas_canisters[i]] / balloon_sizes[i]
        balloon_fractions.append(balloon_fraction)
    return balloon_fractions

def get_maximum_balloon_fraction(balloon_fractions):
    return max(balloon_fractions)

def main():
    n = int(input())
    balloon_sizes = get_balloon_sizes(n)
    gas_canisters = get_gas_canisters(n)
    gas_canister_amounts = get_gas_canister_amounts(n)
    assigned_gas_canisters = assign_gas_canisters(balloon_sizes, gas_canisters, gas_canister_amounts)
    balloon_fractions = get_balloon_fractions(balloon_sizes, assigned_gas_canisters, gas_canister_amounts)
    maximum_balloon_fraction = get_maximum_balloon_fraction(balloon_fractions)
    print(maximum_balloon_fraction)

if __name__ == '__main__':
    main()

