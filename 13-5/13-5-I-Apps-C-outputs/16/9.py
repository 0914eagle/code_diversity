
def solve(N, u, parent):
    # Initialize variables
    L = 0
    M = 0
    visited = [False] * (N + 1)
    path = []

    # Function to check if the path is nondecreasing and has the correct length
    def is_valid_path(path):
        nonlocal L
        nonlocal M
        if len(path) > L:
            L = len(path)
            M = 1
        elif len(path) == L:
            M += 1
        return L == len(path) and all(u[path[i]] <= u[path[i + 1]] for i in range(len(path) - 1))

    # Function to find all jumping paths in the tree
    def find_paths(node):
        nonlocal visited
        nonlocal path
        visited[node] = True
        path.append(node)
        if is_valid_path(path):
            return
        for child in parent[node]:
            if not visited[child]:
                find_paths(child)
        path.pop()
        visited[node] = False

    # Find all jumping paths in the tree
    find_paths(1)

    # Return the length of the longest jumping path and the number of jumping paths modulo 11092019
    return L, M % 11092019

