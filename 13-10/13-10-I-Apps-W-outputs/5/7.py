
def get_shortest_distance(distances, s, t):
    # Add the distance between the last and first station to the list of distances
    distances.append(distances[0])
    
    # Initialize the minimum distance and the current station
    min_distance = float('inf')
    current_station = s
    
    # Loop through the distances and find the minimum distance between the current station and the target station
    for i in range(len(distances)):
        if current_station == t:
            break
        current_station = (current_station + 1) % len(distances)
        min_distance = min(min_distance, distances[current_station])
    
    return min_distance

def main():
    n = int(input())
    distances = list(map(int, input().split()))
    s, t = map(int, input().split())
    print(get_shortest_distance(distances, s, t))

if __name__ == '__main__':
    main()

