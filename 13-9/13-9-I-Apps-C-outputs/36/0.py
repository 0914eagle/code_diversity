
def solve(A, B, N, conveyors):
    # Initialize the minimum time to travel from A to B
    min_time = 0
    
    # Loop through each conveyor
    for conveyor in conveyors:
        # Calculate the distance from A to the start of the conveyor
        dist_start = distance(A, conveyor[0])
        # Calculate the distance from A to the end of the conveyor
        dist_end = distance(A, conveyor[1])
        # Calculate the total distance on the conveyor
        total_dist = distance(conveyor[0], conveyor[1])
        # Calculate the time to travel on the conveyor
        time_conveyor = total_dist / 2
        # Calculate the time to travel from A to the start of the conveyor
        time_start = dist_start / 1
        # Calculate the time to travel from the end of the conveyor to B
        time_end = distance(B, conveyor[1]) / 1
        # Calculate the total time to travel on the conveyor
        total_time = time_start + time_conveyor + time_end
        # If the total time is less than the current minimum time, update the minimum time
        if total_time < min_time or min_time == 0:
            min_time = total_time
    
    # Return the minimum time to travel from A to B
    return min_time

# Function to calculate the distance between two points
def distance(A, B):
    return ((B[0]-A[0])**2 + (B[1]-A[1])**2)**0.5

