
import math

def get_input():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    return K, N, A

def solve(K, N, A):
    # Calculate the distance from each house to the northmost point of the pond
    distances = [abs(A[i] - K) for i in range(N)]
    
    # Sort the distances in ascending order
    sorted_distances = sorted(distances)
    
    # Calculate the minimum distance needed to visit all houses
    min_distance = 0
    for i in range(N):
        min_distance += sorted_distances[i]
    
    return min_distance

def main():
    K, N, A = get_input()
    print(solve(K, N, A))

if __name__ == '__main__':
    main()

