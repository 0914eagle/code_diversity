
def read_input():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    return K, N, A

def solve(K, N, A):
    # Initialize the distance array with the distance from the ith house to the northmost point
    dist = [abs(A[i] - K) for i in range(N)]
    
    # Loop through each house and update the distance array
    for i in range(N):
        for j in range(N):
            if i != j:
                dist[i] = min(dist[i], dist[j] + abs(A[i] - A[j]))
    
    # Return the minimum distance needed to visit all the houses
    return min(dist)

def main():
    K, N, A = read_input()
    print(solve(K, N, A))

if __name__ == '__main__':
    main()

