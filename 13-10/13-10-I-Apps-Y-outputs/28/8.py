
def read_input():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    return K, N, A

def minimum_distance(K, N, A):
    # Initialize the minimum distance to travel as 0
    min_dist = 0
    
    # Iterate through the houses and calculate the distance traveled
    for i in range(N):
        # Calculate the distance traveled from the current house to the next house
        dist = (A[i] - A[(i+1)%N]) % K
        if dist > (K/2):
            dist = K - dist
        min_dist += dist
    
    return min_dist

def main():
    K, N, A = read_input()
    print(minimum_distance(K, N, A))

if __name__ == '__main__':
    main()

