
def get_minimum_time(N, A, B, C, D, E):
    # Initialize the number of people at each city
    num_people = [N, 0, 0, 0, 0, 0]
    
    # Initialize the time needed to travel from one city to the next
    time_needed = [0, 1, 1, 1, 1, 1]
    
    # Initialize the maximum number of people that can travel at each time
    max_people = [A, B, C, D, E]
    
    # Initialize the minimum time needed to travel from City 1 to City 6
    min_time = 0
    
    # Loop until all the people have reached City 6
    while num_people[-1] < N:
        # Find the city with the most people
        most_populated_city = num_people.index(max(num_people))
        
        # Calculate the number of people that can travel at each time
        num_travelers = [min(max_people[i], num_people[i]) for i in range(most_populated_city)]
        
        # Update the number of people at each city
        num_people = [num_people[i] - num_travelers[i] for i in range(most_populated_city)] + [num_travelers[-1]]
        
        # Update the time needed to travel from the current city to the next city
        time_needed = [time_needed[i] + 1 for i in range(most_populated_city)] + [0]
        
        # Update the minimum time needed to travel from City 1 to City 6
        min_time += max(time_needed)
    
    return min_time

def main():
    N, A, B, C, D, E = map(int, input().split())
    print(get_minimum_time(N, A, B, C, D, E))

if __name__ == '__main__':
    main()

