
def get_moves(n, stones, matrix):
    # Initialize the number of moves to 0
    moves = 0
    # Initialize the list of moves to be returned
    move_list = []
    # Initialize the list of vertices that are not yet occupied by a stone
    available_vertices = [i for i in range(1, n+1) if i not in stones]
    # While there are still available vertices
    while available_vertices:
        # Get the next available vertex
        next_vertex = available_vertices[0]
        # Get the color of the diagonal connecting the next vertex to the current vertex
        color = matrix[next_vertex][stones[0]]
        # If the color is not '*'
        if color != '*':
            # Get the index of the vertex that is connected to the next vertex by the same color
            connected_vertex = [i for i in range(1, n+1) if matrix[next_vertex][i] == color][0]
            # Move the stone from the next vertex to the connected vertex
            move_list.append((next_vertex, connected_vertex))
            # Update the list of available vertices
            available_vertices.remove(next_vertex)
            available_vertices.remove(connected_vertex)
        # Increment the number of moves
        moves += 1
    # Return the number of moves and the list of moves
    return moves, move_list

def main():
    # Read the input
    n = int(input())
    stones = [int(i) for i in input().split()]
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    # Get the moves
    moves, move_list = get_moves(n, stones, matrix)
    # Print the number of moves
    print(moves)
    # Print the moves
    for move in move_list:
        print(*move)

if __name__ == '__main__':
    main()

