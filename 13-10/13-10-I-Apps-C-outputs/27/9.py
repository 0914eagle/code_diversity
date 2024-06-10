
def get_universities_pairs(n, k, u_indices):
    # Initialize a list to store the pairs of universities
    university_pairs = []
    # Iterate through the list of university indices
    for i in range(k):
        # Get the current university index
        current_university = u_indices[i]
        # Get the next university index
        next_university = u_indices[(i + 1) % k]
        # Add the pair of universities to the list
        university_pairs.append((current_university, next_university))
    return university_pairs

def get_total_distance(n, university_pairs):
    # Initialize a variable to store the total distance
    total_distance = 0
    # Iterate through the list of university pairs
    for pair in university_pairs:
        # Get the current university index
        current_university = pair[0]
        # Get the next university index
        next_university = pair[1]
        # Calculate the distance between the current and next university
        distance = get_distance(n, current_university, next_university)
        # Add the distance to the total distance
        total_distance += distance
    return total_distance

def get_distance(n, town1, town2):
    # Initialize a variable to store the distance
    distance = 0
    # Iterate through the list of roads
    for road in roads:
        # Get the current road
        current_road = road[0]
        # Get the next road
        next_road = road[1]
        # Check if the current road connects the two towns
        if (current_road == town1 and next_road == town2) or (current_road == town2 and next_road == town1):
            # Increment the distance
            distance += 1
    return distance

def main():
    # Read the input
    n, k = map(int, input().split())
    u_indices = list(map(int, input().split()))
    roads = []
    for i in range(n - 1):
        x, y = map(int, input().split())
        roads.append((x, y))
    # Get the university pairs
    university_pairs = get_universities_pairs(n, k, u_indices)
    # Get the total distance
    total_distance = get_total_distance(n, university_pairs)
    # Print the result
    print(total_distance)

if __name__ == '__main__':
    main()

