
def get_minimum_time(N, A, B, C, D, E):
    # Initialize the number of people at each city
    num_people = [N, 0, 0, 0, 0, 0]
    
    # Initialize the time
    time = 0
    
    # Loop until all people reach City 6
    while num_people[-1] < N:
        # Get the maximum number of people that can be transported from City 1 to City 2
        max_people = min(A, num_people[0])
        # Add the number of people transported to City 2
        num_people[1] += max_people
        # Subtract the number of people transported from City 1
        num_people[0] -= max_people
        # Increment the time
        time += 1
        
        # Repeat the process for Cities 2 to 5
        for i in range(2, 6):
            # Get the maximum number of people that can be transported from the current city to the next city
            max_people = min(num_people[i-1], globals()[f'{i}'])
            # Add the number of people transported to the next city
            num_people[i%6] += max_people
            # Subtract the number of people transported from the current city
            num_people[i-1] -= max_people
            # Increment the time
            time += 1
    
    # Return the minimum time required for all people to reach City 6
    return time

def main():
    # Read the input
    N, A, B, C, D, E = map(int, input().split())
    
    # Get the minimum time required for all people to reach City 6
    time = get_minimum_time(N, A, B, C, D, E)
    
    # Print the minimum time
    print(time)

if __name__ == '__main__':
    main()

