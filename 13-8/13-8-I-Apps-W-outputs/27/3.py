
def get_zoo_data(n, m):
    # Function to get the data for the zoo
    areas = []
    roads = []
    
    for i in range(n):
        areas.append(int(input()))
    
    for i in range(m):
        x, y = map(int, input().split())
        roads.append((x, y))
    
    return areas, roads

def get_min_animal_count(areas, roads):
    # Function to get the minimum animal count for each pair of areas
    min_animal_count = {}
    
    for i in range(len(areas)):
        for j in range(i+1, len(areas)):
            min_animal_count[(i+1, j+1)] = min(areas[i], areas[j])
    
    return min_animal_count

def get_avg_min_animal_count(areas, roads):
    # Function to get the average minimum animal count for all pairs of areas
    min_animal_count = get_min_animal_count(areas, roads)
    total = 0
    count = 0
    
    for i in range(len(areas)):
        for j in range(i+1, len(areas)):
            total += min_animal_count[(i+1, j+1)]
            count += 1
    
    return total / count

if __name__ == '__main__':
    n, m = map(int, input().split())
    areas, roads = get_zoo_data(n, m)
    print(get_avg_min_animal_count(areas, roads))

