
def get_final_coordinates(plants, directions):
    current_coordinates = plants[0]
    for direction in directions:
        if direction == "A":
            current_coordinates = (current_coordinates[0] + 1, current_coordinates[1] + 1)
        elif direction == "B":
            current_coordinates = (current_coordinates[0] + 1, current_coordinates[1] - 1)
        elif direction == "C":
            current_coordinates = (current_coordinates[0] - 1, current_coordinates[1] + 1)
        elif direction == "D":
            current_coordinates = (current_coordinates[0] - 1, current_coordinates[1] - 1)
        if current_coordinates not in plants:
            break
    return current_coordinates

def main():
    num_plants, num_jumps = map(int, input().split())
    directions = input()
    plants = []
    for i in range(num_plants):
        x, y = map(int, input().split())
        plants.append((x, y))
    final_coordinates = get_final_coordinates(plants, directions)
    print(final_coordinates[0], final_coordinates[1])

if __name__ == '__main__':
    main()

