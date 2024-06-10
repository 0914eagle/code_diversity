
def get_energy_distribution(lamp_positions, lamp_energies):
    positive_energy = 0
    negative_energy = 0
    for lamp_position, lamp_energy in zip(lamp_positions, lamp_energies):
        if lamp_energy > 0:
            positive_energy += lamp_energy
        else:
            negative_energy += lamp_energy
    return positive_energy, negative_energy

def find_balancing_line(lamp_positions, lamp_energies):
    positive_energy, negative_energy = get_energy_distribution(lamp_positions, lamp_energies)
    if positive_energy == negative_energy:
        return 0

    min_distance = float('inf')
    for i in range(len(lamp_positions)):
        for j in range(i+1, len(lamp_positions)):
            distance = get_distance(lamp_positions[i], lamp_positions[j])
            if distance < min_distance:
                min_distance = distance
                balancing_line = [lamp_positions[i], lamp_positions[j]]

    return balancing_line

def get_distance(position1, position2):
    return ((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2) ** 0.5

def main():
    lamp_positions = []
    lamp_energies = []
    for _ in range(int(input())):
        x, y, e = map(int, input().split())
        lamp_positions.append((x, y))
        lamp_energies.append(e)
    balancing_line = find_balancing_line(lamp_positions, lamp_energies)
    if balancing_line:
        print(get_distance(balancing_line[0], balancing_line[1]))
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()

