
def get_energy_sources(lamp_coordinates, lamp_energies):
    positive_energy_sources = []
    negative_energy_sources = []
    for lamp_coordinate, lamp_energy in zip(lamp_coordinates, lamp_energies):
        if lamp_energy > 0:
            positive_energy_sources.append(lamp_coordinate)
        else:
            negative_energy_sources.append(lamp_coordinate)
    return positive_energy_sources, negative_energy_sources

def get_shortest_line_balancing_energy(positive_energy_sources, negative_energy_sources):
    min_distance = float('inf')
    for positive_energy_source in positive_energy_sources:
        for negative_energy_source in negative_energy_sources:
            distance = get_distance(positive_energy_source, negative_energy_source)
            if distance < min_distance:
                min_distance = distance
    return min_distance

def get_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def main():
    num_lamps = int(input())
    lamp_coordinates = []
    lamp_energies = []
    for i in range(num_lamps):
        x, y, energy = map(int, input().split())
        lamp_coordinates.append((x, y))
        lamp_energies.append(energy)
    positive_energy_sources, negative_energy_sources = get_energy_sources(lamp_coordinates, lamp_energies)
    shortest_line_balancing_energy = get_shortest_line_balancing_energy(positive_energy_sources, negative_energy_sources)
    print(shortest_line_balancing_energy)

if __name__ == '__main__':
    main()

