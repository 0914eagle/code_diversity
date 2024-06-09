
def solve(N, u, p):
    # Initialize variables
    L = 1
    M = 0
    visited = [False] * (N + 1)
    stack = []

    # Start from the root
    stack.append(1)
    visited[1] = True

    while stack:
        # Pop a vertex from the stack
        vertex = stack.pop()

        # Check if the vertex has a non-decreasing label
        if u[vertex] >= u[p[vertex]]:
            L = max(L, visited.count(True))
            M += 1

        # Add the vertex's children to the stack
        for i in range(N + 1):
            if p[i] == vertex and not visited[i]:
                stack.append(i)
                visited[i] = True

    return L, M % 11092019

