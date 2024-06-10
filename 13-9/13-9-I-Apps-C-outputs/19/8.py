
import math

def get_line_length(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_circuit_length(lamp_positions, lamp_energies):
    circuit_length = 0
    for i in range(len(lamp_positions)):
        for j in range(i+1, len(lamp_positions)):
            x1, y1 = lamp_positions[i]
            x2, y2 = lamp_positions[j]
            energy = lamp_energies[i] * lamp_energies[j]
            if energy < 0:
                circuit_length += get_line_length(x1, y1, x2, y2)
    return circuit_length

def find_min_circuit_length(lamp_positions, lamp_energies):
    min_circuit_length = float('inf')
    for i in range(len(lamp_positions)):
        for j in range(i+1, len(lamp_positions)):
            x1, y1 = lamp_positions[i]
            x2, y2 = lamp_positions[j]
            energy = lamp_energies[i] * lamp_energies[j]
            if energy < 0:
                circuit_length = get_line_length(x1, y1, x2, y2)
                if circuit_length < min_circuit_length:
                    min_circuit_length = circuit_length
    return min_circuit_length

def main():
    num_lamps = int(input())
    lamp_positions = []
    lamp_energies = []
    for i in range(num_lamps):
        x, y, energy = map(int, input().split())
        lamp_positions.append((x, y))
        lamp_energies.append(energy)
    min_circuit_length = find_min_circuit_length(lamp_positions, lamp_energies)
    if min_circuit_length == float('inf'):
        print("IMPOSSIBLE")
    else:
        print(min_circuit_length)

if __name__ == '__main__':
    main()

