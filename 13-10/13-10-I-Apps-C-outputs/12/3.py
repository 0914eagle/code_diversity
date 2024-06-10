
def get_input():
    N = int(input())
    L, W = map(int, input().split())
    positions = []
    for _ in range(N):
        positions.append(int(input()))
    return N, L, W, positions

def move_trees(N, L, W, positions):
    # Initialize the distance matrix
    distance = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            distance[i][j] = abs(positions[i] - positions[j])
    
    # Fill in the rest of the distance matrix
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    # Find the minimum distance by checking the diagonal of the distance matrix
    min_distance = float('inf')
    for i in range(N):
        min_distance = min(min_distance, distance[i][i])
    
    return min_distance

def main():
    N, L, W, positions = get_input()
    print(move_trees(N, L, W, positions))

if __name__ == '__main__':
    main()

