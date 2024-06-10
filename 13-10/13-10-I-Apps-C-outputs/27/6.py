
def get_min_distance(graph, pairs):
    # Calculate the total distance between pairs
    total_distance = 0
    for pair in pairs:
        total_distance += graph[pair[0]][pair[1]]
    return total_distance

def make_pairs(graph, k):
    # Initialize the pairs list
    pairs = []
    # Iterate through the graph
    for i in range(len(graph)):
        # Check if the current town is not already in a pair
        if i not in pairs:
            # Iterate through the rest of the graph
            for j in range(i+1, len(graph)):
                # Check if the current town is not already in a pair
                if j not in pairs:
                    # Calculate the distance between the current town and the next town
                    distance = graph[i][j]
                    # Check if the distance is not zero
                    if distance != 0:
                        # Add the current pair to the pairs list
                        pairs.append([i, j])
                        # Break the loop if the required number of pairs is reached
                        if len(pairs) == k:
                            break
            # Break the loop if the required number of pairs is reached
            if len(pairs) == k:
                break
    return pairs

def main():
    # Read the input
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    # Initialize the pairs list
    pairs = []
    # Make the pairs
    pairs = make_pairs(graph, k)
    # Calculate the minimum distance
    min_distance = get_min_distance(graph, pairs)
    # Print the result
    print(min_distance)

if __name__ == '__main__':
    main()

