
def get_energy_balance(lamp_positions, lamp_energies):
    # Calculate the total energy of the room
    total_energy = sum(lamp_energies)

    # Initialize the shortest continuous line dividing the positive and negative energy sources
    shortest_line_length = float('inf')

    # Iterate over all possible lines
    for i in range(len(lamp_positions)):
        for j in range(i+1, len(lamp_positions)):
            # Calculate the length of the line
            line_length = ((lamp_positions[i][0] - lamp_positions[j][0]) ** 2 + (lamp_positions[i][1] - lamp_positions[j][1]) ** 2) ** 0.5

            # Calculate the total energy on both sides of the line
            positive_energy = 0
            negative_energy = 0
            for k in range(len(lamp_positions)):
                if k != i and k != j:
                    distance = ((lamp_positions[k][0] - lamp_positions[i][0]) ** 2 + (lamp_positions[k][1] - lamp_positions[i][1]) ** 2) ** 0.5
                    if distance < line_length:
                        positive_energy += lamp_energies[k]
                    else:
                        negative_energy += lamp_energies[k]

            # Check if the total energy on both sides is equal
            if abs(positive_energy - negative_energy) < 1e-6:
                # If it is, update the shortest line length
                shortest_line_length = min(shortest_line_length, line_length)

    # Return the shortest line length or "IMPOSSIBLE" if no such line exists
    if shortest_line_length == float('inf'):
        return "IMPOSSIBLE"
    else:
        return shortest_line_length

def main():
    # Read the number of lamps
    n = int(input())

    # Read the lamp positions and energies
    lamp_positions = []
    lamp_energies = []
    for i in range(n):
        x, y, e = map(int, input().split())
        lamp_positions.append((x, y))
        lamp_energies.append(e)

    # Calculate the energy balance
    energy_balance = get_energy_balance(lamp_positions, lamp_energies)

    # Print the result
    print(energy_balance)

if __name__ == '__main__':
    main()

