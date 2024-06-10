
def get_min_time(N, A, B, C, D, E):
    # Initialize the number of people at each city
    num_people = [N, 0, 0, 0, 0, 0]
    
    # Initialize the time required to travel from each city
    time_required = [0, 1, 1, 1, 1, 1]
    
    # Initialize the maximum number of people that can be transported by each means of transport
    max_capacity = [A, B, C, D, E]
    
    # Initialize the total time required to transport all the people
    total_time = 0
    
    # Loop until all the people reach City 6
    while num_people[-1] < N:
        # Find the city with the maximum number of people
        max_city = num_people.index(max(num_people))
        
        # Find the means of transport that can transport the maximum number of people from the maximum city
        transport_index = max_capacity.index(max(max_capacity[:max_city+1]))
        
        # Transport the maximum number of people from the maximum city to the next city
        num_people[max_city] -= max_capacity[transport_index]
        num_people[max_city+1] += max_capacity[transport_index]
        
        # Increment the time required to transport the people
        time_required[max_city+1] += 1
        
        # Increment the total time required to transport all the people
        total_time += 1
    
    # Return the total time required to transport all the people
    return total_time

def main():
    # Read the input from stdin
    N, A, B, C, D, E = map(int, input().split())
    
    # Call the get_min_time function and print the result
    print(get_min_time(N, A, B, C, D, E))

if __name__ == '__main__':
    main()

