
def get_min_moves(n, stones):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    # Initialize the optimal sequence of moves
    optimal_sequence = []
    
    # Iterate over all possible sequences of moves
    for sequence in itertools.permutations(range(1, n + 1)):
        # Initialize the current number of moves to 0
        current_moves = 0
        # Initialize the current configuration of stones
        current_configuration = list(stones)
        
        # Iterate over all moves in the current sequence
        for move in sequence:
            # Get the current stone and the destination vertex
            current_stone, destination_vertex = move
            # Get the color of the diagonal between the current stone and the destination vertex
            diagonal_color = get_diagonal_color(current_configuration, current_stone, destination_vertex)
            # If the diagonal color is not None, move the stone to the destination vertex
            if diagonal_color is not None:
                current_configuration[current_stone - 1] = destination_vertex
                current_moves += 1
            # If the diagonal color is None, break the loop and try the next sequence
            else:
                break
        
        # If the current configuration of stones is [1, 2, 3], update the minimum number of moves and the optimal sequence of moves
        if current_configuration == [1, 2, 3]:
            min_moves = current_moves
            optimal_sequence = sequence
    
    # Return the minimum number of moves and the optimal sequence of moves
    return min_moves, optimal_sequence

def get_diagonal_color(configuration, stone, destination_vertex):
    # Get the current stone and the destination vertex
    current_stone, destination_vertex = stone, destination_vertex
    # Get the color of the diagonal between the current stone and the destination vertex
    diagonal_color = configuration[current_stone - 1]
    # If the diagonal color is not None, return it
    if diagonal_color is not None:
        return diagonal_color
    # If the diagonal color is None, try to move the stone to the next vertex
    else:
        # Get the next vertex in the sequence
        next_vertex = (current_stone + 1) % len(configuration) + 1
        # Recursively call the function to move the stone to the next vertex
        return get_diagonal_color(configuration, next_vertex, destination_vertex)

def main():
    # Read the input n and the initial configuration of stones
    n = int(input())
    stones = list(map(int, input().split()))
    
    # Get the minimum number of moves and the optimal sequence of moves
    min_moves, optimal_sequence = get_min_moves(n, stones)
    
    # If the minimum number of moves is infinity, there is no way to put the stones on vertices 1, 2, and 3
    if min_moves == float('inf'):
        print(-1)
    # Otherwise, print the minimum number of moves and the optimal sequence of moves
    else:
        print(min_moves)
        for move in optimal_sequence:
            print(*move)

if __name__ == '__main__':
    main()

