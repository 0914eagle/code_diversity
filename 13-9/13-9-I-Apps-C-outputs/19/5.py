
import math

def get_energy_contribution(x, y, e):
    return e

def get_closest_positive_energy_source(x, y, e_list):
    min_distance = math.inf
    closest_energy_source = None
    for e in e_list:
        distance = math.sqrt((x-e[0])**2 + (y-e[1])**2)
        if distance < min_distance:
            min_distance = distance
            closest_energy_source = e
    return closest_energy_source

def get_closest_negative_energy_source(x, y, e_list):
    min_distance = math.inf
    closest_energy_source = None
    for e in e_list:
        distance = math.sqrt((x-e[0])**2 + (y-e[1])**2)
        if distance < min_distance and e[2] < 0:
            min_distance = distance
            closest_energy_source = e
    return closest_energy_source

def get_balancing_line(lamp_coords, lamp_energies):
    positive_energy_sources = []
    negative_energy_sources = []
    for coord, energy in zip(lamp_coords, lamp_energies):
        if energy > 0:
            positive_energy_sources.append(coord)
        else:
            negative_energy_sources.append(coord)
    
    min_distance = math.inf
    balancing_line = None
    for p in positive_energy_sources:
        for n in negative_energy_sources:
            distance = math.sqrt((p[0]-n[0])**2 + (p[1]-n[1])**2)
            if distance < min_distance:
                min_distance = distance
                balancing_line = [p, n]
    return balancing_line

def main():
    num_lamps = int(input())
    lamp_coords = []
    lamp_energies = []
    for i in range(num_lamps):
        x, y, e = map(int, input().split())
        lamp_coords.append((x, y))
        lamp_energies.append(e)
    
    balancing_line = get_balancing_line(lamp_coords, lamp_energies)
    if balancing_line is None:
        print("IMPOSSIBLE")
    else:
        print(balancing_line)

if __name__ == '__main__':
    main()

