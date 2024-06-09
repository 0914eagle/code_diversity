
def f1(N, B, x, y):
    # Initialize a 2D array to store the number of moves required to defuse each bomb
    moves = [[0] * N for _ in range(N)]
    
    # Loop through each bomb and calculate the minimum number of moves required to defuse it
    for i in range(B):
        moves[x[i] - 1][y[i] - 1] = 1
        if x[i] == 1 or x[i] == N or y[i] == 1 or y[i] == N:
            moves[x[i] - 1][y[i] - 1] = 0
    
    # Calculate the total number of moves required to defuse all the bombs
    total_moves = 0
    for i in range(N):
        for j in range(N):
            total_moves += moves[i][j]
    
    return total_moves

def f2(N, B, x, y):
    # Initialize a 2D array to store the number of moves required to defuse each bomb
    moves = [[0] * N for _ in range(N)]
    
    # Loop through each bomb and calculate the minimum number of moves required to defuse it
    for i in range(B):
        moves[x[i] - 1][y[i] - 1] = 1
        if x[i] == 1 or x[i] == N or y[i] == 1 or y[i] == N:
            moves[x[i] - 1][y[i] - 1] = 0
    
    # Calculate the total number of moves required to defuse all the bombs
    total_moves = 0
    for i in range(N):
        for j in range(N):
            total_moves += moves[i][j]
    
    return total_moves

if __name__ == '__main__':
    N, B = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(f1(N, B, x, y))
    print(f2(N, B, x, y))

