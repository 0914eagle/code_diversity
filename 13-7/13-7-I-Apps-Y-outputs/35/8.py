
def find_minimum_time(N, A, B, C, D, E):
    # Initialize the number of people at each city
    num_people = [N, 0, 0, 0, 0, 0]
    
    # Initialize the minimum time required to reach City 6
    min_time = 0
    
    # Loop until all people reach City 6
    while num_people[-1] < N:
        # Find the city with the most people
        max_index = num_people.index(max(num_people))
        
        # Determine the number of people who can travel from the current city to the next city
        if max_index == 0:
            num_travelers = min(A, N)
        elif max_index == 1:
            num_travelers = min(B, num_people[1])
        elif max_index == 2:
            num_travelers = min(C, num_people[2])
        elif max_index == 3:
            num_travelers = min(D, num_people[3])
        else:
            num_travelers = min(E, num_people[4])
        
        # Update the number of people at each city
        num_people[max_index] -= num_travelers
        num_people[max_index + 1] += num_travelers
        
        # Increment the minimum time required to reach City 6
        min_time += 1
    
    return min_time

def main():
    N, A, B, C, D, E = map(int, input().split())
    print(find_minimum_time(N, A, B, C, D, E))

if __name__ == '__main__':
    main()

