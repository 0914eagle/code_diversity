
def read_input():
    N = int(input())
    L, W = map(int, input().split())
    positions = []
    for i in range(N):
        positions.append(int(input()))
    return N, L, W, positions

def solve(N, L, W, positions):
    # Calculate the distance between each pair of trees
    distances = [(positions[i+1] - positions[i])**2 for i in range(N-1)]
    
    # Calculate the total distance by summing up the distances between each pair of trees
    total_distance = sum(distances)
    
    return total_distance

def main():
    N, L, W, positions = read_input()
    result = solve(N, L, W, positions)
    print(result)

if __name__ == '__main__':
    main()

