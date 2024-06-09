
def get_unused_switches(n, m, cables):
    # Initialize a dictionary to store the distances from switch 1 to each other switch
    distances = {1: 0}
    for i in range(2, n+1):
        distances[i] = float('inf')

    # Loop through each cable and calculate the distance from switch 1 to each other switch
    for a, b, length in cables:
        if a not in distances or b not in distances:
            continue
        distances[b] = min(distances[b], distances[a] + length)

    # Find the switches that are not part of the optimal path
    unused_switches = []
    for i in range(1, n+1):
        if i not in distances or distances[i] == float('inf'):
            unused_switches.append(i)

    return len(unused_switches), sorted(unused_switches)

