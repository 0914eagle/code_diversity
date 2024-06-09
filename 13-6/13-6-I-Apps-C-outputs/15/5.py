
def get_final_coordinates(plant_locations, jump_directions):
    final_coordinates = plant_locations[0]
    for i in range(1, len(plant_locations)):
        current_coordinates = plant_locations[i]
        previous_coordinates = plant_locations[i - 1]
        jump_direction = jump_directions[i - 1]
        if jump_direction == "A":
            final_coordinates = (current_coordinates[0] + previous_coordinates[0], current_coordinates[1] + previous_coordinates[1])
        elif jump_direction == "B":
            final_coordinates = (current_coordinates[0] + previous_coordinates[0], current_coordinates[1] - previous_coordinates[1])
        elif jump_direction == "C":
            final_coordinates = (current_coordinates[0] - previous_coordinates[0], current_coordinates[1] + previous_coordinates[1])
        elif jump_direction == "D":
            final_coordinates = (current_coordinates[0] - previous_coordinates[0], current_coordinates[1] - previous_coordinates[1])
    return final_coordinates

def main():
    num_plants, num_jumps = map(int, input().split())
    jump_directions = input()
    plant_locations = []
    for i in range(num_plants):
        x, y = map(int, input().split())
        plant_locations.append((x, y))
    final_coordinates = get_final_coordinates(plant_locations, jump_directions)
    print(final_coordinates[0], final_coordinates[1])

if __name__ == '__main__':
    main()

