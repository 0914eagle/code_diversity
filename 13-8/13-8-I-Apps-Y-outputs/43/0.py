
def get_good_observatories(n, m, heights, roads):
    # Initialize a dictionary to store the elevation of each observatory
    observatories = {i: heights[i-1] for i in range(1, n+1)}
    
    # Loop through each road and update the elevation of the observatories it connects
    for road in roads:
        observatories[road[0]] = min(observatories[road[0]], observatories[road[1]])
        observatories[road[1]] = min(observatories[road[1]], observatories[road[0]])
    
    # Return the number of observatories with the highest elevation
    return len([height for height in observatories.values() if height == max(observatories.values())])

def main():
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))
    roads = [list(map(int, input().split())) for _ in range(m)]
    print(get_good_observatories(n, m, heights, roads))

if __name__ == '__main__':
    main()

