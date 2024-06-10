
def get_input():
    n = int(input())
    distances = list(map(int, input().split()))
    s, t = map(int, input().split())
    return n, distances, s, t

def get_shortest_distance(distances, s, t):
    if s == t:
        return 0
    
    total_distance = 0
    current_station = s
    visited_stations = set()
    
    while True:
        visited_stations.add(current_station)
        next_station = (current_station + 1) % len(distances)
        total_distance += distances[current_station]
        
        if next_station == t:
            break
        
        current_station = next_station
    
    return total_distance

def main():
    n, distances, s, t = get_input()
    print(get_shortest_distance(distances, s, t))

if __name__ == '__main__':
    main()

