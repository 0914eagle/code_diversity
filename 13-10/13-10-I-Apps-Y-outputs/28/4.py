
def get_distance(A):
    # Calculate the cumulative sum of the distances from the starting point
    C = [0] + [A[i] - A[i-1] for i in range(1, len(A))]
    # Find the minimum distance by calculating the sum of the distances between each pair of houses
    return min(sum(C[i:i+2]) for i in range(len(A)))

def solve(K, N, A):
    # Check if the input is valid
    if not 2 <= K <= 10**6:
        raise ValueError("K must be between 2 and 10^6")
    if not 2 <= N <= 2*10**5:
        raise ValueError("N must be between 2 and 2*10^5")
    if len(set(A)) != len(A):
        raise ValueError("There are duplicate values in A")
    if any(not 0 <= a < K for a in A):
        raise ValueError("All values in A must be between 0 and K-1")

    # Find the minimum distance by calculating the sum of the distances between each pair of houses
    return get_distance(A)

if __name__ == '__main__':
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(K, N, A))

