
def f1(N, W_list, H_list, map_list):
    # Initialize a dictionary to store the map pieces
    map_dict = {}
    for i in range(N):
        map_dict[i+1] = map_list[i]

    # Initialize a list to store the reconstructed map
    reconstructed_map = []

    # Loop through the map pieces and add them to the reconstructed map
    for i in range(N):
        for j in range(H_list[i]):
            for k in range(W_list[i]):
                reconstructed_map.append(map_dict[i+1][j][k])

    # Return the reconstructed map
    return reconstructed_map

def f2(reconstructed_map):
    # Initialize a list to store the indices of the map pieces
    indices = []

    # Loop through the reconstructed map and add the indices of the map pieces
    for i in range(len(reconstructed_map)):
        indices.append(i%10)

    # Return the indices of the map pieces
    return indices

if __name__ == '__main__':
    # Read the input from stdin
    N = int(input())
    W_list = []
    H_list = []
    map_list = []
    for i in range(N):
        W, H = map(int, input().split())
        W_list.append(W)
        H_list.append(H)
        map_list.append([input() for _ in range(H)])

    # Call the first function to reconstruct the map
    reconstructed_map = f1(N, W_list, H_list, map_list)

    # Call the second function to get the indices of the map pieces
    indices = f2(reconstructed_map)

    # Print the width and height of the reconstructed map
    print(W, H)

    # Print the reconstructed map
    for i in range(H):
        print("".join(reconstructed_map[i*W:(i+1)*W]))

    # Print the indices of the map pieces
    print("-"*W)
    for i in range(H):
        print("".join(indices[i*W:(i+1)*W]))

