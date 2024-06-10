
def get_max_distance(n, k, u_locations, roads):
    # Initialize the distance matrix with 0s
    distance_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Fill in the distance matrix using the road information
    for road in roads:
        distance_matrix[road[0] - 1][road[1] - 1] = 1
        distance_matrix[road[1] - 1][road[0] - 1] = 1

    # Find the maximum distance by finding the maximum distance between any two universities
    max_distance = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_distance = max(max_distance, distance_matrix[i][j])

    # Return the maximum distance
    return max_distance

def get_university_pairs(n, k, u_locations):
    # Initialize the pairs list
    pairs = []

    # Fill in the pairs list using the university locations
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append([i, j])

    # Shuffle the pairs list to randomize the order
    import random
    random.shuffle(pairs)

    # Return the first k pairs
    return pairs[:k]

def get_total_distance(pairs, distance_matrix):
    # Initialize the total distance to 0
    total_distance = 0

    # Calculate the distance between each pair of universities
    for pair in pairs:
        total_distance += distance_matrix[pair[0]][pair[1]]

    # Return the total distance
    return total_distance

def solve(n, k, u_locations, roads):
    # Get the maximum distance between any two universities
    max_distance = get_max_distance(n, k, u_locations, roads)

    # Get the university pairs
    pairs = get_university_pairs(n, k, u_locations)

    # Get the total distance between the pairs
    total_distance = get_total_distance(pairs, distance_matrix)

    # Return the maximum total distance
    return total_distance

def main():
    # Read the input
    n, k = map(int, input().split())
    u_locations = list(map(int, input().split()))
    roads = []
    for i in range(n - 1):
        x, y = map(int, input().split())
        roads.append([x, y])

    # Solve the problem
    result = solve(n, k, u_locations, roads)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

