
def get_final_coordinates(plants, directions):
    current_coordinates = plants[0]
    for direction in directions:
        next_coordinates = get_next_coordinates(current_coordinates, direction)
        if next_coordinates is not None:
            current_coordinates = next_coordinates
    return current_coordinates

def get_next_coordinates(current_coordinates, direction):
    if direction == "A":
        return (current_coordinates[0] + 1, current_coordinates[1] + 1)
    elif direction == "B":
        return (current_coordinates[0] + 1, current_coordinates[1] - 1)
    elif direction == "C":
        return (current_coordinates[0] - 1, current_coordinates[1] + 1)
    elif direction == "D":
        return (current_coordinates[0] - 1, current_coordinates[1] - 1)
    else:
        return None

if __name__ == '__main__':
    num_plants, num_attempts = map(int, input().split())
    directions = input()
    plants = []
    for i in range(num_plants):
        x, y = map(int, input().split())
        plants.append((x, y))
    final_coordinates = get_final_coordinates(plants, directions)
    print(final_coordinates[0], final_coordinates[1])

