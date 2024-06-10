
def get_division(n, k, town_list, road_list):
    # Initialize the division as a list of pairs
    division = []
    
    # Loop through each university and find the closest university that is not already in a pair
    for i in range(n):
        closest_university = None
        closest_distance = float('inf')
        for j in range(n):
            if j != i and (j, i) not in division:
                distance = get_distance(town_list[j], town_list[i], road_list)
                if distance < closest_distance:
                    closest_university = j
                    closest_distance = distance
        division.append((i, closest_university))
    
    # Return the division as a list of pairs
    return division

def get_distance(town1, town2, road_list):
    # Initialize the distance as infinity
    distance = float('inf')
    
    # Loop through each road and find the shortest path between the two towns
    for road in road_list:
        if town1 in road and town2 in road:
            distance = min(distance, road[0] + road[1])
    
    # Return the shortest path as the distance
    return distance

def main():
    n, k = map(int, input().split())
    town_list = []
    road_list = []
    for i in range(n):
        town_list.append(int(input()))
    for i in range(n - 1):
        x, y = map(int, input().split())
        road_list.append((x, y))
    
    division = get_division(n, k, town_list, road_list)
    distance = 0
    for pair in division:
        distance += get_distance(town_list[pair[0]], town_list[pair[1]], road_list)
    print(distance)

if __name__ == '__main__':
    main()

