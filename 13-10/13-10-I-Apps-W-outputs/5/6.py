
def get_shortest_distance(distances, s, t):
    # Add the distance between the last and first station to the list of distances
    distances.append(distances[0])
    
    # Initialize the shortest distance as infinity
    shortest_distance = float('inf')
    
    # Iterate over the distances between pairs of neighboring stations
    for i in range(len(distances)):
        # Check if the current distance is the shortest distance between s and t
        if distances[i] + distances[(i + 1) % len(distances)] < shortest_distance:
            shortest_distance = distances[i] + distances[(i + 1) % len(distances)]
    
    return shortest_distance

def main():
    # Read the number of stations and the distances between pairs of neighboring stations
    n = int(input())
    distances = [int(x) for x in input().split()]
    
    # Read the numbers of the starting and ending stations
    s, t = map(int, input().split())
    
    # Find the shortest distance between the starting and ending stations
    shortest_distance = get_shortest_distance(distances, s, t)
    
    # Print the shortest distance
    print(shortest_distance)

if __name__ == '__main__':
    main()

