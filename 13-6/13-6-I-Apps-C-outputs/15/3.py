
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
    plants = []
    directions = []
    for _ in range(int(input())):
        plants.append(tuple(map(int, input().split())))
    directions = list(input())
    final_coordinates = get_final_coordinates(plants, directions)
    print(*final_coordinates)

if __name__ == '__main__':
    main()

