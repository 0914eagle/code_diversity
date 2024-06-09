
def f1(map_pieces):
    # Function to rearrange the map pieces to form a valid rectangular map
    ...
    return rearranged_map

def f2(rearranged_map):
    # Function to rotate the rearranged map to form a valid rectangular map
    ...
    return rotated_map

def f3(rotated_map):
    # Function to find the treasure location in the rotated map
    ...
    return treasure_location

def main():
    # Read input from stdin
    num_map_pieces = int(input())
    map_pieces = []
    for i in range(num_map_pieces):
        width, height = map(int, input().split())
        map_pieces.append([input() for _ in range(height)])

    # Rearrange the map pieces to form a valid rectangular map
    rearranged_map = f1(map_pieces)

    # Rotate the rearranged map to form a valid rectangular map
    rotated_map = f2(rearranged_map)

    # Find the treasure location in the rotated map
    treasure_location = f3(rotated_map)

    # Print the width and height of the reconstructed map
    print(f"{rearranged_map[0][0]} {rearranged_map[0][1]}")

    # Print the reconstructed map
    for row in rearranged_map:
        print("".join(row))

    # Print the hyphens
    print("-" * len(rearranged_map[0]))

    # Print the map piece indices
    for row in rearranged_map:
        print("".join(str(map_pieces.index(row) + 1) for row in rearranged_map))

if __name__ == '__main__':
    main()

