
import math

def get_energy_grid(lamp_positions):
    # Initialize an empty energy grid with zeros
    energy_grid = [[0] * 100 for _ in range(100)]

    # Fill in the energy grid with the lamp positions and energies
    for lamp in lamp_positions:
        x, y, energy = lamp
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                energy_grid[i][j] += energy

    return energy_grid

def find_balancing_line(lamp_positions):
    # Get the energy grid for the lamp positions
    energy_grid = get_energy_grid(lamp_positions)

    # Find the shortest continuous line that divides the energy grid into positive and negative parts
    for i in range(1, 99):
        for j in range(1, 99):
            if energy_grid[i][j] != 0 and energy_grid[i-1][j] * energy_grid[i][j-1] < 0:
                return i + j

    return "IMPOSSIBLE"

def main():
    num_lamps = int(input())
    lamp_positions = []
    for _ in range(num_lamps):
        x, y, energy = map(int, input().split())
        lamp_positions.append((x, y, energy))

    print(find_balancing_line(lamp_positions))

if __name__ == '__main__':
    main()

