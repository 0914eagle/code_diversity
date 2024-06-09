
def is_valid_network(D):
    N = len(D)
    if N < 2:
        return "NO"
    # Check if the number of rooms is valid
    if any(D[i] < 1 or D[i] > N - 1 for i in range(N)):
        return "NO"
    # Check if the number of tunnels is valid
    if sum(D) != N - 1:
        return "NO"
    # Check if the network is connected
    visited = set([1])
    queue = [1]
    while queue:
        current = queue.pop(0)
        for i in range(1, N + 1):
            if i not in visited and D[current - 1] >= i:
                visited.add(i)
                queue.append(i)
    if len(visited) == N:
        return "YES"
    else:
        return "NO"

