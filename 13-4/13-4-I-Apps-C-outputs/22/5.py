
def f1(map_pieces):
    # Function to reconstruct the treasure map from the given map pieces
    ...
    return reconstructed_map

def f2(reconstructed_map):
    # Function to find the location of the treasure in the reconstructed map
    ...
    return treasure_location

if __name__ == '__main__':
    # Read input from stdin
    num_map_pieces = int(input())
    map_pieces = []
    for i in range(num_map_pieces):
        width, height = map(int, input().split())
        map_pieces.append(input())

    # Reconstruct the treasure map
    reconstructed_map = f1(map_pieces)

    # Find the location of the treasure in the reconstructed map
    treasure_location = f2(reconstructed_map)

    # Print the width and height of the reconstructed map
    print(reconstructed_map.shape[1], reconstructed_map.shape[0])

    # Print the reconstructed map
    for i in range(reconstructed_map.shape[0]):
        print("".join(map(str, reconstructed_map[i])))

    # Print the map piece indices
    for i in range(reconstructed_map.shape[0]):
        print("-" * reconstructed_map.shape[1])
        print("".join(map(str, map_pieces.index(reconstructed_map[i]) + 1)))

