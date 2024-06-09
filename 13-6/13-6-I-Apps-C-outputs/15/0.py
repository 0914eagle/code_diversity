
def f1(N, K, directions, plants):
    # Initialize a dictionary to store the coordinates of the plants
    plant_coordinates = {}
    for i in range(N):
        x, y = plants[i]
        plant_coordinates[(x, y)] = i

    # Initialize a list to store the coordinates of the final plant
    final_plant = []

    # Iterate through the directions and update the coordinates of the final plant
    for direction in directions:
        if direction == "A":
            final_plant.append((final_plant[0] + 1, final_plant[1] + 1))
        elif direction == "B":
            final_plant.append((final_plant[0] + 1, final_plant[1] - 1))
        elif direction == "C":
            final_plant.append((final_plant[0] - 1, final_plant[1] + 1))
        elif direction == "D":
            final_plant.append((final_plant[0] - 1, final_plant[1] - 1))

    # Return the final coordinates of the plant
    return plant_coordinates[tuple(final_plant)]

def f2(N, K, directions, plants):
    # Initialize a dictionary to store the coordinates of the plants
    plant_coordinates = {}
    for i in range(N):
        x, y = plants[i]
        plant_coordinates[(x, y)] = i

    # Initialize a list to store the coordinates of the final plant
    final_plant = []

    # Iterate through the directions and update the coordinates of the final plant
    for direction in directions:
        if direction == "A":
            final_plant.append((final_plant[0] + 1, final_plant[1] + 1))
        elif direction == "B":
            final_plant.append((final_plant[0] + 1, final_plant[1] - 1))
        elif direction == "C":
            final_plant.append((final_plant[0] - 1, final_plant[1] + 1))
        elif direction == "D":
            final_plant.append((final_plant[0] - 1, final_plant[1] - 1))

    # Return the final coordinates of the plant
    return plant_coordinates[tuple(final_plant)]

if __name__ == '__main__':
    N, K = map(int, input().split())
    directions = input()
    plants = []
    for i in range(N):
        x, y = map(int, input().split())
        plants.append((x, y))
    print(f1(N, K, directions, plants))
    print(f2(N, K, directions, plants))

