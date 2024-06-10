
def get_shortest_time(W, v_h, N, gates, skis):
    # Initialize the shortest time to infinity
    shortest_time = float('inf')
    # Iterate over all possible pairs of skis
    for s in skis:
        # Initialize the current time to 0
        current_time = 0
        # Iterate over all gates
        for i in range(N):
            # Calculate the distance between the current gate and the previous gate
            distance = abs(gates[i][0] - gates[i-1][0])
            # Calculate the time it takes to travel the distance at the current speed
            time = distance / s
            # Add the time it takes to travel the distance to the current time
            current_time += time
            # Check if the current time is greater than the shortest time
            if current_time > shortest_time:
                # If it is, break out of the loop and move on to the next pair of skis
                break
        # If we reach the end of all gates without breaking, set the shortest time to the current time
        else:
            shortest_time = current_time
    # Return the shortest time
    return shortest_time

def get_skis(W, v_h, N, gates):
    # Initialize the shortest time to infinity
    shortest_time = float('inf')
    # Initialize the list of skis to use
    skis = []
    # Iterate over all possible speeds
    for s in range(1, v_h+1):
        # Calculate the time it takes to travel the distance at the current speed
        time = W / s
        # Check if the time is less than the shortest time
        if time < shortest_time:
            # If it is, set the shortest time to the current time and add the current speed to the list of skis to use
            shortest_time = time
            skis.append(s)
    # Return the list of skis to use
    return skis

def main():
    # Read the input
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
    # Get the list of skis to use
    skis = get_skis(W, v_h, N, gates)
    # Get the shortest time
    shortest_time = get_shortest_time(W, v_h, N, gates, skis)
    # Print the output
    if shortest_time == float('inf'):
        print("IMPOSSIBLE")
    else:
        print(shortest_time)

if __name__ == '__main__':
    main()

