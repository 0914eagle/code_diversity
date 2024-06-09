
import math

def get_energy_contribution(x, y, e):
    return e

def get_line_length(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_shortest_line_dividing_energy_sources(lamp_positions, lamp_energies):
    shortest_line_length = float('inf')
    shortest_line_coordinates = None
    for i in range(len(lamp_positions)):
        for j in range(i+1, len(lamp_positions)):
            x1, y1 = lamp_positions[i]
            x2, y2 = lamp_positions[j]
            e1 = lamp_energies[i]
            e2 = lamp_energies[j]
            line_length = get_line_length(x1, y1, x2, y2)
            if e1*e2 < 0 and line_length < shortest_line_length:
                shortest_line_length = line_length
                shortest_line_coordinates = (x1, y1, x2, y2)
    if shortest_line_coordinates is None:
        return "IMPOSSIBLE"
    return shortest_line_length

def main():
    num_lamps = int(input())
    lamp_positions = []
    lamp_energies = []
    for i in range(num_lamps):
        x, y, e = map(int, input().split())
        lamp_positions.append((x, y))
        lamp_energies.append(get_energy_contribution(x, y, e))
    print(get_shortest_line_dividing_energy_sources(lamp_positions, lamp_energies))

if __name__ == '__main__':
    main()

