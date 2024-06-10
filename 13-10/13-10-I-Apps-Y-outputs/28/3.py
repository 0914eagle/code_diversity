
def read_input():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    return K, N, A

def solve(K, N, A):
    # Initialize the distance array with infinity
    dist = [float('inf')] * (N + 1)
    # Initialize the previous array with -1
    prev = [-1] * (N + 1)
    # Initialize the queue with the first house
    queue = [(0, 0)]
    # Loop until the queue is empty
    while queue:
        # Get the current house and distance from the queue
        house, distance = queue.pop(0)
        # If the current house is not already visited
        if dist[house] > distance:
            # Update the distance and previous array
            dist[house] = distance
            prev[house] = house
            # Add the neighboring houses to the queue
            for i in range(1, N + 1):
                if A[house] + A[i] < K:
                    queue.append((i, distance + A[i]))
    # Find the minimum distance
    min_distance = min(dist[1:])
    # Initialize the current house
    current_house = 1
    # Loop until the current house is the starting house
    while current_house != 0:
        # Update the current house
        current_house = prev[current_house]
        # Add the distance of the current house to the minimum distance
        min_distance += A[current_house]
    return min_distance

def main():
    K, N, A = read_input()
    print(solve(K, N, A))

if __name__ == '__main__':
    main()

