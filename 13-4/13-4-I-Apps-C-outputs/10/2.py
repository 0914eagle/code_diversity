
import math

def get_energy_contribution(x, y, e):
    return e

def get_energy_balance(lamp_positions, lamp_energies):
    total_energy = 0
    for i in range(len(lamp_positions)):
        total_energy += get_energy_contribution(lamp_positions[i][0], lamp_positions[i][1], lamp_energies[i])
    return total_energy

def get_shortest_balance_line(lamp_positions, lamp_energies):
    min_distance = math.inf
    for i in range(len(lamp_positions)):
        for j in range(i+1, len(lamp_positions)):
            distance = math.sqrt((lamp_positions[i][0] - lamp_positions[j][0])**2 + (lamp_positions[i][1] - lamp_positions[j][1])**2)
            if distance < min_distance:
                min_distance = distance
    return min_distance

def get_balance_line_length(lamp_positions, lamp_energies):
    balance_line_length = get_shortest_balance_line(lamp_positions, lamp_energies)
    return balance_line_length

def main():
    lamp_positions = []
    lamp_energies = []
    for i in range(int(input())):
        x, y, e = map(int, input().split())
        lamp_positions.append((x, y))
        lamp_energies.append(e)
    balance_line_length = get_balance_line_length(lamp_positions, lamp_energies)
    print(balance_line_length)

if __name__ == '__main__':
    main()

