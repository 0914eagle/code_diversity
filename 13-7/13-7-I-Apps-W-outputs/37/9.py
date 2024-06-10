
def get_maximum_sum(n, a, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Find the prize with the highest pleasantness
    max_pleasantness = max(a)

    # Initialize a set to store the gifts that hang on the first gift
    gifts = set([1])

    # Loop through the gifts and add them to the set if they hang on the first gift
    for i in range(2, n + 1):
        if 1 in graph[i]:
            gifts.add(i)

    # Initialize a variable to store the maximum sum of pleasantness
    max_sum = 0

    # Loop through the gifts and find the pair with the maximum sum of pleasantness
    for i in gifts:
        for j in gifts:
            if i != j:
                sum_pleasantness = a[i] + a[j]
                if sum_pleasantness > max_sum:
                    max_sum = sum_pleasantness

    # If the maximum sum of pleasantness is greater than the maximum pleasantness of a single gift, return it
    if max_sum > max_pleasantness:
        return max_sum
    else:
        return "Impossible"

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_maximum_sum(n, a, edges))

if __name__ == '__main__':
    main()

