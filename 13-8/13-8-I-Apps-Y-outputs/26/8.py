
def get_earliest_time(A, B, C, D, E):
    # Calculate the time it takes to serve each dish
    time_to_serve = [A, B, C, D, E]
    
    # Initialize the earliest time for the last dish to be delivered as the sum of the time it takes to serve all dishes
    earliest_time = sum(time_to_serve)
    
    # Loop through each dish and calculate the earliest time it can be served
    for i in range(len(time_to_serve)):
        # Calculate the time it takes to serve the current dish
        current_time = time_to_serve[i]
        
        # Calculate the time it takes to serve the previous dishes
        previous_times = time_to_serve[:i]
        previous_time = sum(previous_times)
        
        # Calculate the earliest time the current dish can be served
        earliest_time_for_current_dish = previous_time + current_time
        
        # Update the earliest time for the last dish if necessary
        if earliest_time_for_current_dish < earliest_time:
            earliest_time = earliest_time_for_current_dish
    
    return earliest_time

def main():
    A, B, C, D, E = map(int, input().split())
    print(get_earliest_time(A, B, C, D, E))

if __name__ == '__main__':
    main()

