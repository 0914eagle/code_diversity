
def get_division_of_pairs(n, k, u_list, roads):
    
    # Initialize the minimum spanning tree
    mst = []
    for i in range(n):
        mst.append([])
    for road in roads:
        x, y = road[0], road[1]
        mst[x - 1].append((y - 1, 1))
        mst[y - 1].append((x - 1, 1))

    # Initialize the pairs of universities
    pairs = []
    for i in range(k):
        pairs.append([u_list[2 * i], u_list[2 * i + 1]])

    # Find the maximum distance between universities in each pair
    max_dist = 0
    for pair in pairs:
        dist = 0
        for i in range(n):
            for j in range(i + 1, n):
                if mst[i][j][0] == pair[0] or mst[i][j][0] == pair[1]:
                    dist += mst[i][j][1]
        max_dist = max(max_dist, dist)

    return max_dist

def get_total_distance(n, k, u_list, roads):
    
    # Initialize the minimum spanning tree
    mst = []
    for i in range(n):
        mst.append([])
    for road in roads:
        x, y = road[0], road[1]
        mst[x - 1].append((y - 1, 1))
        mst[y - 1].append((x - 1, 1))

    # Initialize the pairs of universities
    pairs = []
    for i in range(k):
        pairs.append([u_list[2 * i], u_list[2 * i + 1]])

    # Calculate the total distance between universities in each pair
    dist = 0
    for pair in pairs:
        for i in range(n):
            for j in range(i + 1, n):
                if mst[i][j][0] == pair[0] or mst[i][j][0] == pair[1]:
                    dist += mst[i][j][1]

    return dist

def main():
    n, k = map(int, input().split())
    u_list = list(map(int, input().split()))
    roads = []
    for i in range(n - 1):
        x, y = map(int, input().split())
        roads.append((x, y))

    # Get the division of universities into pairs
    pairs = get_division_of_pairs(n, k, u_list, roads)

    # Calculate the total distance between universities in the pairs
    dist = get_total_distance(n, k, u_list, roads)

    # Print the maximum possible sum of distances in the division of universities into k pairs
    print(dist)

if __name__ == '__main__':
    main()

