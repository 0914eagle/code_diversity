
import itertools

def get_energy_sources(lamp_coordinates, lamp_energies):
    
    return list(zip(lamp_coordinates, lamp_energies))

def get_balanced_line(energy_sources):
    
    # Sort the energy sources by their x-coordinate
    energy_sources.sort(key=lambda x: x[0])
    
    # Initialize the total energy and the current sum of energies
    total_energy = sum(energy_source[1] for energy_source in energy_sources)
    current_sum = 0
    
    # Iterate through the energy sources and find the shortest line that divides them into two parts with equal total energy
    for i in range(len(energy_sources)):
        current_sum += energy_sources[i][1]
        if current_sum == total_energy / 2:
            return abs(energy_sources[i][0] - energy_sources[i-1][0])
    
    # If no such line exists, return IMPOSSIBLE
    return "IMPOSSIBLE"

def get_balanced_line_brute_force(energy_sources):
    
    # Get all possible lines
    all_lines = []
    for energy_source in energy_sources:
        all_lines.append(energy_source[0])
    
    # Sort the lines and find the shortest one that divides the energy sources into two parts with equal total energy
    all_lines.sort()
    for line in all_lines:
        energy_sources_left = []
        energy_sources_right = []
        for energy_source in energy_sources:
            if energy_source[0] < line:
                energy_sources_left.append(energy_source[1])
            else:
                energy_sources_right.append(energy_source[1])
        if sum(energy_sources_left) == sum(energy_sources_right):
            return line
    
    # If no such line exists, return IMPOSSIBLE
    return "IMPOSSIBLE"

def main():
    lamp_coordinates = []
    lamp_energies = []
    for _ in range(int(input())):
        x, y, e = map(int, input().split())
        lamp_coordinates.append((x, y))
        lamp_energies.append(e)
    
    energy_sources = get_energy_sources(lamp_coordinates, lamp_energies)
    print(get_balanced_line(energy_sources))

if __name__ == '__main__':
    main()

