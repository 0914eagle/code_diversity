
import sys
import math

def get_input():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    return K, N, A

def solve(K, N, A):
    # Calculate the sum of the distances between each pair of houses
    distances = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            distances[i] += min(abs(A[i] - A[j]), K - abs(A[i] - A[j]))
    
    # Return the minimum distance
    return min(distances)

def main():
    K, N, A = get_input()
    print(solve(K, N, A))

if __name__ == '__main__':
    main()

