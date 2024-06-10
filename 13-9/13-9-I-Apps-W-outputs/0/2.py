
def get_min_a_dfs(a, n, k):
    # Initialize the minimum a_i as the maximum possible value
    min_a = 1000001
    # Initialize the number of nodes visited as 0
    num_visited = 0
    # Initialize the stack with the root node
    stack = [1]
    # Loop until the stack is empty
    while stack:
        # Pop a node from the stack
        node = stack.pop()
        # If the node has not been visited before, visit it and update the minimum a_i if necessary
        if node not in a:
            a[node] = 0
            num_visited += 1
            if num_visited <= k:
                min_a = min(min_a, a[node])
        # Push the node's neighbors onto the stack
        stack += [neighbor for neighbor in a[node] if neighbor not in a]
    # Return the minimum a_i
    return min_a

def get_max_grade(a, n, k):
    # Initialize the maximum grade as 0
    max_grade = 0
    # Loop through all possible roots
    for root in range(1, n + 1):
        # Get the minimum a_i of the first k nodes in a DFS-order traversal of the tree with the current root
        min_a = get_min_a_dfs(a, n, k)
        # Update the maximum grade if the current root's minimum a_i is greater than the current maximum grade
        max_grade = max(max_grade, min_a)
    # Return the maximum grade
    return max_grade

def main():
    n, k = map(int, input().split())
    a = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)
    print(get_max_grade(a, n, k))

if __name__ == '__main__':
    main()

