
def get_barica_coordinates(plants, directions):
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
    with open("input.txt", "r") as f:
        N, K = map(int, f.readline().split())
        directions = f.readline().strip()
        for _ in range(N):
            x, y = map(int, f.readline().split())
            plants.append((x, y))
    print(get_barica_coordinates(plants, directions))

if __name__ == '__main__':
    main()

