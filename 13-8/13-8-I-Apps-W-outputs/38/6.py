
def get_number_of_bridges(a, b, c):
    # Initialize a 2D array to store the number of bridges between each pair of islands
    num_bridges = [[0 for _ in range(a)] for _ in range(a)]
    
    # Initialize a 2D array to store the number of bridges between each pair of islands with the same color
    num_same_color_bridges = [[0 for _ in range(a)] for _ in range(a)]
    
    # Initialize a set to store the indices of the islands with the same color
    same_color_islands = set()
    
    # Iterate over each island and its neighbors
    for i in range(a):
        for j in range(i+1, a):
            # If the two islands have the same color, increment the number of bridges between them
            if i // (a // 3) == j // (a // 3):
                num_bridges[i][j] = 1
                num_same_color_bridges[i][j] = 1
                same_color_islands.add(i)
                same_color_islands.add(j)
    
    # Iterate over each island and its neighbors with the same color
    for i in range(a):
        for j in range(i+1, a):
            # If the two islands have the same color and are not connected by a bridge, increment the number of bridges between them
            if i // (a // 3) == j // (a // 3) and num_same_color_bridges[i][j] == 0:
                num_bridges[i][j] = 1
    
    # Iterate over each island and its neighbors with a different color
    for i in range(a):
        for j in range(a):
            # If the two islands have a different color and are not connected by a bridge, increment the number of bridges between them
            if i // (a // 3) != j // (a // 3) and num_same_color_bridges[i][j] == 0:
                num_bridges[i][j] = 1
    
    # Calculate the total number of bridges
    total_bridges = 0
    for i in range(a):
        for j in range(a):
            total_bridges += num_bridges[i][j]
    
    # Return the total number of bridges modulo 998 244 353
    return total_bridges % 998244353

def main():
    a, b, c = map(int, input().split())
    print(get_number_of_bridges(a, b, c))

if __name__ == '__main__':
    main()

