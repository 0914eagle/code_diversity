
def get_good_observatories(num_observatories, num_roads, observatory_elevations, road_pairs):
    # Initialize a dictionary to store the elevations of the observatories that can be reached from each observatory
    reachable_elevations = {}
    for observatory in range(1, num_observatories + 1):
        reachable_elevations[observatory] = set()
    
    # Iterate over the roads to find the elevations of the observatories that can be reached from each observatory
    for road in road_pairs:
        observatory1, observatory2 = road[0], road[1]
        reachable_elevations[observatory1].add(observatory2)
        reachable_elevations[observatory2].add(observatory1)
    
    # Initialize a set to store the good observatories
    good_observatories = set()
    
    # Iterate over the observatories and check if they are good
    for observatory in range(1, num_observatories + 1):
        # If the elevation of the current observatory is higher than the elevations of all the observatories that can be reached from it, it is good
        if observatory_elevations[observatory - 1] > max(reachable_elevations[observatory]):
            good_observatories.add(observatory)
    
    return len(good_observatories)

def main():
    num_observatories, num_roads = map(int, input().split())
    observatory_elevations = list(map(int, input().split()))
    road_pairs = [list(map(int, input().split())) for _ in range(num_roads)]
    print(get_good_observatories(num_observatories, num_roads, observatory_elevations, road_pairs))

if __name__ == '__main__':
    main()

