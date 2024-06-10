
def input_data():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    return K, N, A

def solve(K, N, A):
    # Sort the distances from smallest to largest
    sorted_A = sorted(A)

    # Initialize the minimum distance to travel
    min_distance = 0

    # Iterate through the distances and calculate the minimum distance to travel
    for i in range(N):
        min_distance += sorted_A[i]

    return min_distance

def main():
    K, N, A = input_data()
    print(solve(K, N, A))

if __name__ == '__main__':
    main()

