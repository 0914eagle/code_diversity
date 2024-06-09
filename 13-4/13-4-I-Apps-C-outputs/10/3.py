
import math

def get_energy_contribution(x, y, e):
    return e

def get_line_length(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_shortest_line_length(lamp_coordinates, lamp_energies):
    shortest_line_length = float('inf')
    for i in range(len(lamp_coordinates)):
        for j in range(i+1, len(lamp_coordinates)):
            x1, y1 = lamp_coordinates[i]
            x2, y2 = lamp_coordinates[j]
            line_length = get_line_length(x1, y1, x2, y2)
            if line_length < shortest_line_length:
                shortest_line_length = line_length
    return shortest_line_length

def main():
    num_lamps = int(input())
    lamp_coordinates = []
    lamp_energies = []
    for i in range(num_lamps):
        x, y, e = map(int, input().split())
        lamp_coordinates.append((x, y))
        lamp_energies.append(get_energy_contribution(x, y, e))
    shortest_line_length = get_shortest_line_length(lamp_coordinates, lamp_energies)
    print(shortest_line_length)

if __name__ == '__main__':
    main()

