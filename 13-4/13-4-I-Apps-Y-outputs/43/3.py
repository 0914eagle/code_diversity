
def get_min_distance(N, K, x_coordinates):
    # Calculate the total distance covered by each robot
    total_distance_A = 0
    total_distance_B = 0
    for i in range(N):
        total_distance_A += abs(x_coordinates[i] - 0) + abs(x_coordinates[i] - K)
        total_distance_B += abs(x_coordinates[i] - K) + abs(x_coordinates[i] - 0)
    
    # Return the minimum total distance
    return min(total_distance_A, total_distance_B)

def main():
    N, K = map(int, input().split())
    x_coordinates = list(map(int, input().split()))
    print(get_min_distance(N, K, x_coordinates))

if __name__ == '__main__':
    main()

