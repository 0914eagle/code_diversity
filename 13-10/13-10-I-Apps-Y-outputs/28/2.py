
def get_input():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    return K, N, A

def solve(K, N, A):
    # Calculate the total distance traveled by visiting all houses
    total_distance = 0
    for i in range(N):
        total_distance += abs(A[i] - A[(i+1)%N])
    
    # Return the minimum distance needed to visit all houses
    return total_distance

def main():
    K, N, A = get_input()
    print(solve(K, N, A))

if __name__ == '__main__':
    main()

