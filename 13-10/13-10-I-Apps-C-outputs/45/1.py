
def get_energy_sources(lamp_coordinates):
    positive_energy_sources = []
    negative_energy_sources = []
    for lamp in lamp_coordinates:
        x, y, energy = lamp
        if energy > 0:
            positive_energy_sources.append((x, y))
        else:
            negative_energy_sources.append((x, y))
    return positive_energy_sources, negative_energy_sources

def get_shortest_line_balancing_energy(positive_energy_sources, negative_energy_sources):
    min_distance = float('inf')
    for positive_source in positive_energy_sources:
        for negative_source in negative_energy_sources:
            distance = get_distance(positive_source, negative_source)
            if distance < min_distance:
                min_distance = distance
    return min_distance

def get_distance(source1, source2):
    x1, y1 = source1
    x2, y2 = source2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def main():
    lamp_coordinates = []
    for _ in range(int(input())):
        lamp_coordinates.append(tuple(map(int, input().split())))
    positive_energy_sources, negative_energy_sources = get_energy_sources(lamp_coordinates)
    line_length = get_shortest_line_balancing_energy(positive_energy_sources, negative_energy_sources)
    print(line_length)

if __name__ == '__main__':
    main()

