
def get_min_time(N, A, B, C, D, E):
    # Initialize the number of people at each city
    num_people = [N, 0, 0, 0, 0, 0]
    
    # Initialize the minimum time required to reach City 6
    min_time = 0
    
    # Loop until all people reach City 6
    while num_people[-1] < N:
        # Find the city with the most people
        max_city = num_people.index(max(num_people))
        
        # Calculate the number of people who can travel in the next minute
        num_travelers = min(num_people[max_city], A if max_city == 0 else B if max_city == 1 else C if max_city == 2 else D if max_city == 3 else E)
        
        # Update the number of people at each city
        num_people[max_city] -= num_travelers
        num_people[max_city + 1] += num_travelers
        
        # Increment the minimum time required to reach City 6
        min_time += 1
    
    return min_time

def main():
    N, A, B, C, D, E = map(int, input().split())
    print(get_min_time(N, A, B, C, D, E))

if __name__ == '__main__':
    main()

