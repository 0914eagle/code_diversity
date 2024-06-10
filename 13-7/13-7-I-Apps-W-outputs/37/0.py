
def get_maximum_sum_of_pleasantness(n, a, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize a set to store the gifts that are chosen by Chloe and Vladik
    chosen_gifts = set()

    # Function to find the maximum sum of pleasantness of the gifts that are chosen by Chloe and Vladik
    def dfs(vertex, parent, pleasantness_sum):
        nonlocal chosen_gifts
        nonlocal maximum_sum

        # If the current vertex is not the first gift, add its pleasantness to the sum
        if vertex != 1:
            pleasantness_sum += a[vertex - 1]

        # If the current vertex is not the first gift and is not already chosen, add it to the set of chosen gifts
        if vertex != 1 and vertex not in chosen_gifts:
            chosen_gifts.add(vertex)

        # If the current vertex is the first gift, return the sum of pleasantness
        if vertex == 1:
            return pleasantness_sum

        # Recursively call the function for all the neighbors of the current vertex
        for neighbor in graph[vertex]:
            if neighbor != parent:
                pleasantness_sum = dfs(neighbor, vertex, pleasantness_sum)

        return pleasantness_sum

    # Initialize the maximum sum of pleasantness
    maximum_sum = 0

    # Call the dfs function for the first gift
    dfs(1, 0, 0)

    # If the set of chosen gifts has only two elements, return the maximum sum of pleasantness
    if len(chosen_gifts) == 2:
        return maximum_sum
    else:
        return "Impossible"

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_maximum_sum_of_pleasantness(n, a, edges))

if __name__ == '__main__':
    main()

