
def f1(N, W_list, H_list, map_list):
    # Initialize a dictionary to store the map pieces
    map_pieces = {}
    for i in range(N):
        map_pieces[i+1] = map_list[i]
    
    # Initialize a list to store the reconstructed map
    reconstructed_map = []
    
    # Loop through the map pieces and add them to the reconstructed map
    for i in range(N):
        current_map = map_pieces[i+1]
        current_width = W_list[i]
        current_height = H_list[i]
        for j in range(current_height):
            for k in range(current_width):
                reconstructed_map.append(current_map[j][k])
    
    # Return the reconstructed map
    return reconstructed_map

def f2(reconstructed_map):
    # Initialize a dictionary to store the map pieces
    map_pieces = {}
    
    # Loop through the reconstructed map and add the corresponding map pieces to the dictionary
    for i in range(len(reconstructed_map)):
        current_value = reconstructed_map[i]
        current_index = i % 10 + 1
        if current_index not in map_pieces:
            map_pieces[current_index] = []
        map_pieces[current_index].append(current_value)
    
    # Return the map pieces
    return map_pieces

if __name__ == '__main__':
    N = int(input())
    W_list = []
    H_list = []
    map_list = []
    for i in range(N):
        W, H = map(int, input().split())
        W_list.append(W)
        H_list.append(H)
        map_list.append(list(input()))
    reconstructed_map = f1(N, W_list, H_list, map_list)
    map_pieces = f2(reconstructed_map)
    print(len(reconstructed_map[0]), len(reconstructed_map))
    for i in range(len(reconstructed_map)):
        print(reconstructed_map[i], end='')
    print()
    for i in range(len(reconstructed_map[0])):
        print('-', end='')
    print()
    for i in range(len(reconstructed_map)):
        print(map_pieces[i%10+1].index(reconstructed_map[i])+1, end='')

