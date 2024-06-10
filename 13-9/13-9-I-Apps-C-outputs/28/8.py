
def get_max_distance(n, k, roads, universities):
    # Initialize the maximum distance to 0
    max_distance = 0
    # Iterate over all possible pairs of universities
    for i in range(k):
        for j in range(i+1, k):
            # Calculate the distance between the current pair of universities
            distance = get_distance(n, roads, universities[i], universities[j])
            # Update the maximum distance if necessary
            if distance > max_distance:
                max_distance = distance
    # Return the maximum distance
    return max_distance

def get_distance(n, roads, university1, university2):
    # Initialize the distance to 0
    distance = 0
    # Iterate over all roads between the two universities
    for road in roads:
        # If the current road connects the two universities, update the distance
        if (road[0] == university1 and road[1] == university2) or (road[0] == university2 and road[1] == university1):
            distance += 1
    # Return the distance
    return distance

def main():
    # Read the input data
    n, k = map(int, input().split())
    roads = []
    universities = []
    for i in range(n - 1):
        x, y = map(int, input().split())
        roads.append((x, y))
    for i in range(k):
        universities.append(int(input()))
    # Call the get_max_distance function to get the maximum distance
    max_distance = get_max_distance(n, k, roads, universities)
    # Print the maximum distance
    print(max_distance)

if __name__ == '__main__':
    main()

