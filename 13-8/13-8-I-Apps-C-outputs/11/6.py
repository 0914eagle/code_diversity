
def get_speed_for_gates(gates, v_h, S):
    # Initialize a dictionary to store the minimum speed required to pass through each gate
    speeds = {}
    for gate in gates:
        speeds[gate] = float('inf')

    # Iterate over the skis and calculate the minimum speed required to pass through each gate
    for s in S:
        for gate in gates:
            if gate[0] - s <= v_h:
                speeds[gate] = min(speeds[gate], s)

    # Return the minimum speed required to pass through all the gates
    return min(speeds.values())

def get_vertical_speed(gates, v_h, S):
    # Get the speed required to pass through each gate
    speeds = get_speed_for_gates(gates, v_h, S)

    # Find the maximum vertical speed required to pass through all the gates
    max_speed = 0
    for gate in gates:
        max_speed = max(max_speed, speeds[gate])

    # Return the maximum vertical speed
    return max_speed

def main():
    # Read the input
    W, v_h, N = map(int, input().split())
    gates = []
    for i in range(N):
        x, y = map(int, input().split())
        gates.append((x, y))
    S = int(input())
    S = list(map(int, input().split()))

    # Get the vertical speed
    v = get_vertical_speed(gates, v_h, S)

    # Check if it is possible to complete the race with any pair of skis
    if v == 0:
        print("IMPOSSIBLE")
    else:
        print(v)

if __name__ == '__main__':
    main()

