
def get_final_coordinates(num_plants, jump_directions, plant_coordinates):
    final_coordinates = [plant_coordinates[0]]
    for i in range(1, num_plants):
        current_coordinates = final_coordinates[i-1]
        jump_direction = jump_directions[i-1]
        if jump_direction == "A":
            next_coordinates = (current_coordinates[0] + 1, current_coordinates[1] + 1)
        elif jump_direction == "B":
            next_coordinates = (current_coordinates[0] + 1, current_coordinates[1] - 1)
        elif jump_direction == "C":
            next_coordinates = (current_coordinates[0] - 1, current_coordinates[1] + 1)
        elif jump_direction == "D":
            next_coordinates = (current_coordinates[0] - 1, current_coordinates[1] - 1)
        final_coordinates.append(next_coordinates)
    return final_coordinates[-1]

def main():
    num_plants, num_jumps = map(int, input().split())
    jump_directions = input()
    plant_coordinates = []
    for i in range(num_plants):
        x, y = map(int, input().split())
        plant_coordinates.append((x, y))
    final_coordinates = get_final_coordinates(num_plants, jump_directions, plant_coordinates)
    print(final_coordinates)

if __name__ == '__main__':
    main()

