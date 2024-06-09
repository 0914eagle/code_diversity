
def f1(N, K, directions, plants):
    # Initialize Barica's current position as the first plant
    current_position = plants[0]

    # Iterate through the directions and update Barica's position accordingly
    for i in range(K):
        direction = directions[i]
        if direction == "A":
            current_position = (current_position[0] + 1, current_position[1] + 1)
        elif direction == "B":
            current_position = (current_position[0] + 1, current_position[1] - 1)
        elif direction == "C":
            current_position = (current_position[0] - 1, current_position[1] + 1)
        elif direction == "D":
            current_position = (current_position[0] - 1, current_position[1] - 1)

    # Return Barica's final position
    return current_position

def f2(N, K, directions, plants):
    # Initialize a dictionary to store the coordinates of the plants
    plant_coordinates = {}
    for i in range(N):
        plant_coordinates[i] = plants[i]

    # Initialize Barica's current position as the first plant
    current_position = plants[0]

    # Iterate through the directions and update Barica's position accordingly
    for i in range(K):
        direction = directions[i]
        if direction == "A":
            current_position = (current_position[0] + 1, current_position[1] + 1)
        elif direction == "B":
            current_position = (current_position[0] + 1, current_position[1] - 1)
        elif direction == "C":
            current_position = (current_position[0] - 1, current_position[1] + 1)
        elif direction == "D":
            current_position = (current_position[0] - 1, current_position[1] - 1)

        # If Barica jumps to a plant that is not in the dictionary, add it to the dictionary
        if current_position not in plant_coordinates:
            plant_coordinates[len(plant_coordinates)] = current_position

    # Return Barica's final position
    return current_position

if __name__ == '__main__':
    N, K = map(int, input().split())
    directions = input()
    plants = []
    for i in range(N):
        x, y = map(int, input().split())
        plants.append((x, y))
    print(f1(N, K, directions, plants))
    print(f2(N, K, directions, plants))

