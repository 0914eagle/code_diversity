
def get_energy_contribution(x, y, e):
    return e

def get_energy_balance(lamp_positions, lamp_energies):
    positive_energy = 0
    negative_energy = 0
    for i in range(len(lamp_positions)):
        x, y, e = lamp_positions[i]
        e = get_energy_contribution(x, y, e)
        if e > 0:
            positive_energy += e
        else:
            negative_energy += e
    return positive_energy, negative_energy

def find_shortest_balancing_line(lamp_positions, lamp_energies):
    min_distance = float('inf')
    for i in range(len(lamp_positions)):
        for j in range(i+1, len(lamp_positions)):
            x1, y1 = lamp_positions[i]
            x2, y2 = lamp_positions[j]
            distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
            if distance < min_distance:
                min_distance = distance
    return min_distance

def main():
    num_lamp_positions = int(input())
    lamp_positions = []
    lamp_energies = []
    for i in range(num_lamp_positions):
        x, y, e = map(int, input().split())
        lamp_positions.append((x, y))
        lamp_energies.append(e)
    positive_energy, negative_energy = get_energy_balance(lamp_positions, lamp_energies)
    if positive_energy == negative_energy:
        print("IMPOSSIBLE")
    else:
        print(find_shortest_balancing_line(lamp_positions, lamp_energies))

if __name__ == '__main__':
    main()

