
import itertools

def get_universities_pairs(universities, n):
    
    # Initialize a list to store the pairs
    pairs = []
    # Iterate over the combinations of universities
    for combination in itertools.combinations(universities, 2):
        # Check if the pair is not already in the list
        if combination not in pairs:
            # Add the pair to the list
            pairs.append(combination)
        # If the list has reached the required number of pairs
        if len(pairs) == n:
            # Break the loop
            break
    # Return the pairs
    return pairs

def get_total_distance(pairs, towns, roads):
    
    # Initialize the total distance to 0
    total_distance = 0
    # Iterate over the pairs
    for pair in pairs:
        # Get the town indices for the current pair
        town_indices = [towns.index(university) for university in pair]
        # Get the distances between the towns in the current pair
        distances = [roads[town_index] for town_index in town_indices]
        # Add the distances to the total distance
        total_distance += sum(distances)
    # Return the total distance
    return total_distance

def main():
    # Read the input
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    towns = list(range(1, n + 1))
    roads = [list(map(int, input().split())) for _ in range(n - 1)]
    # Get the maximum total distance
    pairs = get_universities_pairs(universities, k)
    total_distance = get_total_distance(pairs, towns, roads)
    # Print the result
    print(total_distance)

if __name__ == '__main__':
    main()

