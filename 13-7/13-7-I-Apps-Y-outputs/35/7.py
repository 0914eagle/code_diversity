
def get_min_time(N, A, B, C, D, E):
    # Initialize the number of people at each city
    num_people = [N, 0, 0, 0, 0, 0]
    
    # Initialize the time required for each transportation method
    time_train = 0
    time_bus = 0
    time_taxi = 0
    time_airplane = 0
    time_ship = 0
    
    # Loop until all people reach City 6
    while num_people[-1] < N:
        # Check if there are any people at City 1 and if the train can accommodate them
        if num_people[0] > 0 and num_people[0] <= A:
            # Add the number of people at City 1 to the number of people at City 2
            num_people[1] += num_people[0]
            # Subtract the number of people at City 1 from the number of people at City 1
            num_people[0] = 0
            # Increment the time required for the train
            time_train += 1
        
        # Check if there are any people at City 2 and if the bus can accommodate them
        if num_people[1] > 0 and num_people[1] <= B:
            # Add the number of people at City 2 to the number of people at City 3
            num_people[2] += num_people[1]
            # Subtract the number of people at City 2 from the number of people at City 2
            num_people[1] = 0
            # Increment the time required for the bus
            time_bus += 1
        
        # Check if there are any people at City 3 and if the taxi can accommodate them
        if num_people[2] > 0 and num_people[2] <= C:
            # Add the number of people at City 3 to the number of people at City 4
            num_people[3] += num_people[2]
            # Subtract the number of people at City 3 from the number of people at City 3
            num_people[2] = 0
            # Increment the time required for the taxi
            time_taxi += 1
        
        # Check if there are any people at City 4 and if the airplane can accommodate them
        if num_people[3] > 0 and num_people[3] <= D:
            # Add the number of people at City 4 to the number of people at City 5
            num_people[4] += num_people[3]
            # Subtract the number of people at City 4 from the number of people at City 4
            num_people[3] = 0
            # Increment the time required for the airplane
            time_airplane += 1
        
        # Check if there are any people at City 5 and if the ship can accommodate them
        if num_people[4] > 0 and num_people[4] <= E:
            # Add the number of people at City 5 to the number of people at City 6
            num_people[5] += num_people[4]
            # Subtract the number of people at City 5 from the number of people at City 5
            num_people[4] = 0
            # Increment the time required for the ship
            time_ship += 1
    
    # Return the minimum time required for all people to reach City 6
    return min(time_train, time_bus, time_taxi, time_airplane, time_ship)

def main():
    # Read the input
    N, A, B, C, D, E = map(int, input().split())
    
    # Call the get_min_time function and print the result
    print(get_min_time(N, A, B, C, D, E))

if __name__ == '__main__':
    main()

