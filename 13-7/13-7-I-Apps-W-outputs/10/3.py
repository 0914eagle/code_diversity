
def get_input():
    n = int(input())
    vertices = list(map(int, input().split()))
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    return n, vertices, matrix

def solve(n, vertices, matrix):
    # Initialize the board
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        board[i][i] = 1
    
    # Initialize the stones
    stones = [0] * 3
    for i in range(3):
        stones[i] = vertices[i]
    
    # Initialize the moves
    moves = []
    
    # Loop through the stones
    for i in range(3):
        # Get the current stone
        current_stone = stones[i]
        
        # Get the neighbors of the current stone
        neighbors = []
        for j in range(n):
            if board[current_stone - 1][j] == 1:
                neighbors.append(j + 1)
        
        # Find the neighbor with the same color as the diagonal connecting the current stone and the other stone
        for neighbor in neighbors:
            if matrix[current_stone - 1][neighbor - 1] == matrix[stones[i % 2] - 1][stones[(i + 1) % 2] - 1]:
                # Move the stone to the neighbor
                stones[i] = neighbor
                moves.append([current_stone, neighbor])
                break
    
    # Check if the stones are on the required vertices
    if stones == [1, 2, 3]:
        return moves
    else:
        return -1

def main():
    n, vertices, matrix = get_input()
    moves = solve(n, vertices, matrix)
    if moves == -1:
        print(-1)
    else:
        print(len(moves))
        for move in moves:
            print(move[0], move[1])

if __name__ == '__main__':
    main()

