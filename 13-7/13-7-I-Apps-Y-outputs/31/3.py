
def get_balloons(n):
    balloons = []
    for i in range(1, n+1):
        balloons.append(i)
    return balloons

def get_gas_canisters(n, capacities):
    gas_canisters = []
    for i in range(n):
        gas_canisters.append(capacities[i])
    return gas_canisters

def assign_gas_canisters(balloons, gas_canisters):
    assigned_balloons = []
    assigned_gas_canisters = []
    for balloon in balloons:
        assigned_balloons.append(balloon)
        assigned_gas_canisters.append(gas_canisters.pop())
    return assigned_balloons, assigned_gas_canisters

def get_balloon_capacities(balloons):
    balloon_capacities = []
    for balloon in balloons:
        balloon_capacities.append(balloon)
    return balloon_capacities

def get_gas_canister_capacities(gas_canisters):
    gas_canister_capacities = []
    for gas_canister in gas_canisters:
        gas_canister_capacities.append(gas_canister)
    return gas_canister_capacities

def get_balloon_helium_contents(balloon_capacities, gas_canister_capacities):
    balloon_helium_contents = []
    for i in range(len(balloon_capacities)):
        balloon_helium_contents.append(gas_canister_capacities[i] / balloon_capacities[i])
    return balloon_helium_contents

def get_maximum_fraction(balloon_helium_contents):
    maximum_fraction = 0
    for helium_content in balloon_helium_contents:
        if helium_content > maximum_fraction:
            maximum_fraction = helium_content
    return maximum_fraction

def main():
    n = int(input())
    capacities = list(map(int, input().split()))
    balloons = get_balloons(n)
    gas_canisters = get_gas_canisters(n, capacities)
    assigned_balloons, assigned_gas_canisters = assign_gas_canisters(balloons, gas_canisters)
    balloon_capacities = get_balloon_capacities(assigned_balloons)
    gas_canister_capacities = get_gas_canister_capacities(assigned_gas_canisters)
    balloon_helium_contents = get_balloon_helium_contents(balloon_capacities, gas_canister_capacities)
    maximum_fraction = get_maximum_fraction(balloon_helium_contents)
    print(maximum_fraction)

if __name__ == '__main__':
    main()

