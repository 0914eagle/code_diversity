
def get_min_time(N, A, B, C, D, E):
    # Initialize the number of people at each city
    num_people = [N, 0, 0, 0, 0, 0]
    
    # Initialize the time needed to travel from one city to the next
    time_needed = [0, 1, 1, 1, 1, 1]
    
    # Initialize the maximum number of people that can be transported at each time
    max_people = [A, B, C, D, E]
    
    # Initialize the minimum time required to reach City 6
    min_time = 0
    
    # Loop until all the people reach City 6
    while num_people[-1] < N:
        # Find the city with the most people
        max_index = num_people.index(max(num_people))
        
        # Find the transportation mode with the least number of people
        min_index = max_index - 1
        while num_people[min_index] >= max_people[min_index]:
            min_index -= 1
        
        # Move the people from the city with the most people to the city with the least people
        num_people[max_index] -= max_people[min_index]
        num_people[min_index] += max_people[min_index]
        
        # Increase the minimum time required to reach City 6
        min_time += time_needed[min_index]
    
    return min_time

def main():
    N, A, B, C, D, E = map(int, input().split())
    print(get_min_time(N, A, B, C, D, E))

if __name__ == '__main__':
    main()

