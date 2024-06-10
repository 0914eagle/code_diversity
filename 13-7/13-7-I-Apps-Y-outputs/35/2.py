
def get_minimum_time(N, A, B, C, D, E):
    # Initialize the variables
    time = 0
    current_city = 1
    num_people = N
    
    # Loop until all people reach City 6
    while num_people > 0:
        # Determine the next city and the number of people who can travel there
        if current_city == 1:
            next_city = 2
            num_travelers = min(A, num_people)
        elif current_city == 2:
            next_city = 3
            num_travelers = min(B, num_people)
        elif current_city == 3:
            next_city = 4
            num_travelers = min(C, num_people)
        elif current_city == 4:
            next_city = 5
            num_travelers = min(D, num_people)
        elif current_city == 5:
            next_city = 6
            num_travelers = min(E, num_people)
        
        # Update the variables
        time += 1
        num_people -= num_travelers
        current_city = next_city
    
    # Return the minimum time
    return time

def main():
    # Read the input
    N, A, B, C, D, E = map(int, input().split())
    
    # Call the function and print the result
    print(get_minimum_time(N, A, B, C, D, E))

if __name__ == '__main__':
    main()

