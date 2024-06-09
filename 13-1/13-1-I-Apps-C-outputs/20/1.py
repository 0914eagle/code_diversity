
def f1(N, W_list, H_list, map_list):
    # Initialize a dictionary to store the map pieces
    map_dict = {}
    for i in range(N):
        map_dict[i+1] = map_list[i]

    # Initialize a list to store the reconstructed map
    reconstructed_map = []

    # Loop through the map pieces and add them to the reconstructed map
    for i in range(N):
        # Get the current map piece
        current_map = map_dict[i+1]

        # Add the current map piece to the reconstructed map
        reconstructed_map.append(current_map)

    # Return the reconstructed map
    return reconstructed_map

def f2(reconstructed_map):
    # Initialize a list to store the map indices
    map_indices = []

    # Loop through the reconstructed map and add the map indices
    for i in range(len(reconstructed_map)):
        # Get the current map piece
        current_map = reconstructed_map[i]

        # Add the map indices to the list
        map_indices.append(i+1)

    # Return the map indices
    return map_indices

if __name__ == '__main__':
    # Test the functions
    N = 3
    W_list = [4, 2, 2]
    H_list = [1, 2, 2]
    map_list = [['2', '1', '2', '3'], ['2', '1'], ['2', '3'], ['1', '0'], ['2', '2'], ['2', '3'], ['1', '2']]
    reconstructed_map = f1(N, W_list, H_list, map_list)
    map_indices = f2(reconstructed_map)
    print(reconstructed_map)
    print('-' * len(reconstructed_map[0]))
    print(map_indices)

