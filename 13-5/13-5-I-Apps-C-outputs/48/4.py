
def f1(n, c, encounters):
    # initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # add edges to the graph based on the encounters
    for a, b, y in encounters:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    # find the minimum spanning tree of the graph
    mst = kruskal(graph)

    # find the year such that all participants in the first part met before that year, and all participants in the second part met in or after that year
    year = find_year(mst, n)

    return year

def find_year(mst, n):
    # initialize the year as the maximum year in the encounters
    year = max(enc[2] for enc in encounters)

    # iterate through the edges of the minimum spanning tree
    for edge in mst:
        # if the edge connects two participants that have never met before, update the year
        if edge[2] > year:
            year = edge[2]

    return year

def kruskal(graph):
    # initialize the minimum spanning tree as an empty list
    mst = []

    # sort the edges of the graph by their weight
    edges = sorted(graph, key=lambda x: x[2])

    # iterate through the edges of the graph
    for edge in edges:
        # if the edge connects two participants that are not in the same subset, add it to the minimum spanning tree
        if find_subset(edge[0]) != find_subset(edge[1]):
            mst.append(edge)
            union_subsets(edge[0], edge[1])

    return mst

def find_subset(participant):
    # find the root of the subset that the participant is in
    root = participant
    while root != subset[root]:
        root = subset[root]

    return root

def union_subsets(participant1, participant2):
    # find the roots of the subsets that the two participants are in
    root1 = find_subset(participant1)
    root2 = find_subset(participant2)

    # if the roots are different, combine the subsets by making the root of the smaller subset the parent of the root of the larger subset
    if root1 != root2:
        if len(subset[root1]) < len(subset[root2]):
            subset[root1] = root2
        else:
            subset[root2] = root1

if __name__ == '__main__':
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(f1(n, c, encounters))

