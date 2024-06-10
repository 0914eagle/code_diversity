
def get_energy_sources(lamp_positions):
    positive_energy = 0
    negative_energy = 0
    for lamp_position in lamp_positions:
        x, y, energy = lamp_position
        if energy > 0:
            positive_energy += energy
        else:
            negative_energy += energy
    return positive_energy, negative_energy

def find_balancing_line(lamp_positions):
    positive_energy, negative_energy = get_energy_sources(lamp_positions)
    if positive_energy == negative_energy:
        return "IMPOSSIBLE"

    sorted_lamp_positions = sorted(lamp_positions, key=lambda x: x[2])
    for i in range(len(sorted_lamp_positions)):
        current_positive_energy = positive_energy
        current_negative_energy = negative_energy
        for j in range(i, len(sorted_lamp_positions)):
            current_positive_energy += sorted_lamp_positions[j][2]
            current_negative_energy -= sorted_lamp_positions[j][2]
            if current_positive_energy == current_negative_energy:
                return sorted_lamp_positions[j][0]
    return "IMPOSSIBLE"

def main():
    num_lamps = int(input())
    lamp_positions = []
    for i in range(num_lamps):
        x, y, energy = map(int, input().split())
        lamp_positions.append((x, y, energy))
    print(find_balancing_line(lamp_positions))

if __name__ == '__main__':
    main()

