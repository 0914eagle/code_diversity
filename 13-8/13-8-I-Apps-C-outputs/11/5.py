
def get_ski_speed(W, v_h, N, left_gates, skis):
    # Initialize the minimum time to pass through all the gates
    min_time = float('inf')
    # Initialize the ski speed that achieves the minimum time
    min_ski_speed = -1
    
    # Iterate over all the skis
    for ski_speed in skis:
        # Initialize the current time to 0
        current_time = 0
        # Iterate over all the gates
        for i in range(N):
            # Calculate the horizontal distance to the next gate
            horizontal_distance = left_gates[i] - W
            # Calculate the time to pass through the current gate
            time = horizontal_distance / v_h
            # Add the time to the current time
            current_time += time
            # Calculate the vertical distance to the next gate
            vertical_distance = left_gates[i + 1] - left_gates[i]
            # Add the vertical distance to the current time
            current_time += vertical_distance / ski_speed
        
        # If the current time is less than the minimum time, update the minimum time and ski speed
        if current_time < min_time:
            min_time = current_time
            min_ski_speed = ski_speed
    
    # Return the minimum ski speed
    return min_ski_speed

def main():
    # Read the input
    W, v_h, N = map(int, input().split())
    left_gates = []
    for i in range(N):
        x, y = map(int, input().split())
        left_gates.append(x)
    S = int(input())
    skis = set(map(int, input().split()))
    
    # Get the ski speed that allows you to get through the race course in the shortest time
    ski_speed = get_ski_speed(W, v_h, N, left_gates, skis)
    
    # Check if it is impossible to complete the race with any pair of skis
    if ski_speed == -1:
        print("IMPOSSIBLE")
    else:
        print(ski_speed)

if __name__ == '__main__':
    main()

