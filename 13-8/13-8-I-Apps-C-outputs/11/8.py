
def read_input():
    W, v_h, N = map(int, input().split())
    gates = []
    for _ in range(N):
        x, y = map(int, input().split())
        gates.append((x, y))
    S = int(input())
    skis = []
    for _ in range(S):
        s = int(input())
        skis.append(s)
    return W, v_h, N, gates, S, skis

def find_shortest_time(W, v_h, N, gates, S, skis):
    # Initialize the minimum time to pass through the course
    min_time = float('inf')
    # Initialize the minimum speed to pass through the course
    min_speed = 0
    # Loop through all possible speeds
    for s in skis:
        # Initialize the current time to 0
        curr_time = 0
        # Loop through all gates
        for i in range(N):
            # Calculate the time to pass through the current gate
            gate_time = (gates[i][1] - gates[i][0]) / s
            # Calculate the horizontal distance to the next gate
            next_x = gates[(i + 1) % N][0]
            # Calculate the time to move horizontally to the next gate
            horiz_time = abs(next_x - gates[i][0]) / v_h
            # Calculate the total time to move through the current gate and horizontally to the next gate
            total_time = gate_time + horiz_time
            # Update the current time
            curr_time += total_time
        # If the current time is less than the minimum time, update the minimum time and speed
        if curr_time < min_time:
            min_time = curr_time
            min_speed = s
    # Return the minimum speed
    return min_speed

def main():
    W, v_h, N, gates, S, skis = read_input()
    print(find_shortest_time(W, v_h, N, gates, S, skis))

if __name__ == '__main__':
    main()

