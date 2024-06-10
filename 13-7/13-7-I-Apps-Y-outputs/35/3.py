
def get_minimum_time(N, A, B, C, D, E):
    # Initialize the number of people at each city
    num_people_at_city = [N, 0, 0, 0, 0, 0]
    
    # Initialize the minimum time required to travel from City 1 to City 6
    min_time = 0
    
    # Loop until all people reach City 6
    while sum(num_people_at_city) > 0:
        # Find the city with the maximum number of people
        max_city = num_people_at_city.index(max(num_people_at_city))
        
        # Find the city that can be reached with the minimum time
        min_time_to_city = [float('inf')] * 6
        for i in range(6):
            if i != max_city and num_people_at_city[i] > 0:
                min_time_to_city[i] = min(min_time_to_city[i], get_min_time_to_city(max_city, i, A, B, C, D, E))
        
        # Update the minimum time required to travel from City 1 to City 6
        min_time += min(min_time_to_city)
        
        # Update the number of people at each city
        for i in range(6):
            if min_time_to_city[i] != float('inf'):
                num_people_at_city[i] += num_people_at_city[max_city] // (min_time_to_city[i] // min_time_to_city[max_city])
                num_people_at_city[max_city] = num_people_at_city[max_city] % (min_time_to_city[i] // min_time_to_city[max_city])
    
    return min_time

def get_min_time_to_city(start_city, end_city, A, B, C, D, E):
    if start_city == end_city:
        return 0
    elif start_city == 1 and end_city == 2:
        return 1
    elif start_city == 2 and end_city == 3:
        return B
    elif start_city == 3 and end_city == 4:
        return C
    elif start_city == 4 and end_city == 5:
        return D
    elif start_city == 5 and end_city == 6:
        return E
    else:
        return float('inf')

if __name__ == '__main__':
    N, A, B, C, D, E = map(int, input().split())
    print(get_minimum_time(N, A, B, C, D, E))

