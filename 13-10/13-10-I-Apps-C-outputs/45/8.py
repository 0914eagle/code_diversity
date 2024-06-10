
def get_energy_contribution(x, y, e):
    return e

def get_energy_balance(n, lamps):
    # Initialize the energy balance to 0
    energy_balance = 0

    # Loop through each lamp and add its energy contribution to the energy balance
    for lamp in lamps:
        energy_balance += get_energy_contribution(lamp[0], lamp[1], lamp[2])

    # Return the energy balance
    return energy_balance

def find_shortest_balancing_line(n, lamps):
    # Initialize the shortest balancing line to infinity
    shortest_balancing_line = float('inf')

    # Loop through each lamp and check if it is the first or last lamp in the list
    for i, lamp in enumerate(lamps):
        # If the lamp is the first or last lamp in the list, skip it
        if i == 0 or i == n - 1:
            continue

        # Get the energy contribution of the lamp
        energy_contribution = get_energy_contribution(lamp[0], lamp[1], lamp[2])

        # Get the energy balance of the current configuration
        energy_balance = get_energy_balance(n, lamps)

        # If the energy balance is equal to 0, return the length of the current lamp
        if energy_balance == 0:
            return lamp[0]

        # If the energy balance is not equal to 0, find the shortest balancing line
        else:
            # Find the length of the shortest balancing line
            shortest_balancing_line = min(shortest_balancing_line, abs(energy_balance / energy_contribution))

    # Return the shortest balancing line
    return shortest_balancing_line

if __name__ == '__main__':
    n = int(input())
    lamps = []

    for i in range(n):
        x, y, e = map(int, input().split())
        lamps.append((x, y, e))

    shortest_balancing_line = find_shortest_balancing_line(n, lamps)

    if shortest_balancing_line == float('inf'):
        print("IMPOSSIBLE")
    else:
        print(shortest_balancing_line)

