
def get_energy_contribution(lamp_positions, lamp_energies):
    energy_contribution = 0
    for lamp_position, lamp_energy in zip(lamp_positions, lamp_energies):
        energy_contribution += lamp_energy
    return energy_contribution

def get_shortest_line_length(lamp_positions, lamp_energies):
    positive_energy_contribution = get_energy_contribution(lamp_positions, lamp_energies)
    negative_energy_contribution = get_energy_contribution(lamp_positions, [-energy for energy in lamp_energies])
    if positive_energy_contribution == negative_energy_contribution:
        return "IMPOSSIBLE"
    else:
        return abs(positive_energy_contribution - negative_energy_contribution)

def main():
    num_lamps = int(input())
    lamp_positions = []
    lamp_energies = []
    for _ in range(num_lamps):
        x, y, energy = map(int, input().split())
        lamp_positions.append((x, y))
        lamp_energies.append(energy)
    print(get_shortest_line_length(lamp_positions, lamp_energies))

if __name__ == '__main__':
    main()

