
def get_distance(towns, universities):
    
    # Initialize variables
    n = len(towns)
    k = len(universities) // 2
    dist = 0
    pairs = []

    # Loop through each pair of universities
    for i in range(k):
        # Get the indices of the two universities in the pair
        u1 = universities[2 * i]
        u2 = universities[2 * i + 1]

        # Get the distance between the two universities
        dist += get_town_distance(towns, u1, u2)

        # Add the pair to the list of pairs
        pairs.append((u1, u2))

    return dist, pairs

def get_town_distance(towns, town1, town2):
    
    return 1

def main():
    # Read input from stdin
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    towns = []
    for _ in range(n - 1):
        x, y = map(int, input().split())
        towns.append((x, y))

    # Get the maximum possible sum of distances in the division of universities into k pairs
    dist, pairs = get_distance(towns, universities)

    # Print the maximum possible sum of distances
    print(dist)

if __name__ == '__main__':
    main()

