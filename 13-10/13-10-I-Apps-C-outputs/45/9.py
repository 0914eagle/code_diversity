
import math

def get_energy_positions(lamp_positions):
    energy_positions = []
    for lamp_position in lamp_positions:
        x, y, energy = lamp_position
        energy_positions.append((x, y, energy))
    return energy_positions

def get_line_coordinates(lamp_positions):
    x_coordinates = [lamp_position[0] for lamp_position in lamp_positions]
    y_coordinates = [lamp_position[1] for lamp_position in lamp_positions]
    return x_coordinates, y_coordinates

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_closest_lamp(x, y, lamp_positions):
    closest_lamp = None
    closest_distance = None
    for lamp_position in lamp_positions:
        distance = get_distance(x, y, lamp_position[0], lamp_position[1])
        if closest_distance is None or distance < closest_distance:
            closest_distance = distance
            closest_lamp = lamp_position
    return closest_lamp

def get_energy_balance(x, y, lamp_positions):
    closest_lamp = get_closest_lamp(x, y, lamp_positions)
    if closest_lamp is None:
        return 0
    x1, y1, energy1 = closest_lamp
    return energy1

def get_line_length(x_coordinates, y_coordinates):
    line_length = 0
    for i in range(len(x_coordinates) - 1):
        x1, y1 = x_coordinates[i], y_coordinates[i]
        x2, y2 = x_coordinates[i + 1], y_coordinates[i + 1]
        line_length += get_distance(x1, y1, x2, y2)
    return line_length

def get_shortest_line(energy_positions):
    x_coordinates, y_coordinates = get_line_coordinates(energy_positions)
    line_length = get_line_length(x_coordinates, y_coordinates)
    for i in range(len(x_coordinates) - 1):
        x1, y1 = x_coordinates[i], y_coordinates[i]
        x2, y2 = x_coordinates[i + 1], y_coordinates[i + 1]
        line_length = get_distance(x1, y1, x2, y2)
        if get_energy_balance(x1, y1, energy_positions) == get_energy_balance(x2, y2, energy_positions):
            return line_length
    return "IMPOSSIBLE"

def main():
    lamp_positions = []
    while True:
        try:
            num_lamps = int(input())
            for _ in range(num_lamps):
                lamp_positions.append(list(map(int, input().split())))
            break
        except EOFError:
            break
    energy_positions = get_energy_positions(lamp_positions)
    line_length = get_shortest_line(energy_positions)
    print(line_length)

if __name__ == "__main__":
    main()

