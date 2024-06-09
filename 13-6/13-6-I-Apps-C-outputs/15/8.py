
def f1(n, k, directions):
    # Initialize a list to store the coordinates of the plants
    plants = []

    # Iterate through the input and add the coordinates of the plants to the list
    for i in range(n):
        x, y = map(int, input().split())
        plants.append((x, y))

    # Initialize a dictionary to store the coordinates of the plants that Barica has visited
    visited = {}

    # Initialize the current coordinates of Barica
    current_x, current_y = plants[0]

    # Iterate through the directions and update the current coordinates of Barica
    for direction in directions:
        if direction == "A":
            current_x += 1
        elif direction == "B":
            current_y += 1
        elif direction == "C":
            current_x -= 1
        elif direction == "D":
            current_y -= 1

        # If the current coordinates are not in the visited dictionary, add them to the dictionary
        if (current_x, current_y) not in visited:
            visited[(current_x, current_y)] = True

    # Return the final coordinates of Barica
    return current_x, current_y

def f2(n, k, directions):
    # Initialize a list to store the coordinates of the plants
    plants = []

    # Iterate through the input and add the coordinates of the plants to the list
    for i in range(n):
        x, y = map(int, input().split())
        plants.append((x, y))

    # Initialize a dictionary to store the coordinates of the plants that Barica has visited
    visited = {}

    # Initialize the current coordinates of Barica
    current_x, current_y = plants[0]

    # Iterate through the directions and update the current coordinates of Barica
    for direction in directions:
        if direction == "A":
            current_x += 1
        elif direction == "B":
            current_y += 1
        elif direction == "C":
            current_x -= 1
        elif direction == "D":
            current_y -= 1

        # If the current coordinates are not in the visited dictionary, add them to the dictionary
        if (current_x, current_y) not in visited:
            visited[(current_x, current_y)] = True

    # Return the final coordinates of Barica
    return current_x, current_y

if __name__ == '__main__':
    n, k = map(int, input().split())
    directions = input()
    print(*f1(n, k, directions))
    print(*f2(n, k, directions))

