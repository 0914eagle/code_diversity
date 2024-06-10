
import math

def get_minimum_spanning_tree(n, edges):
    # Kruskal's algorithm
    mst = []
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        if find_set(edge[0], mst) != find_set(edge[1], mst):
            mst.append(edge)
            union_sets(edge[0], edge[1], mst)
    return mst

def find_set(u, mst):
    if u == mst[u][0]:
        return u
    else:
        mst[u][0] = find_set(mst[u][0], mst)
        return mst[u][0]

def union_sets(u, v, mst):
    root_u = find_set(u, mst)
    root_v = find_set(v, mst)
    if root_u > root_v:
        mst[root_u][0] = root_v
    else:
        mst[root_v][0] = root_u

def max_distance_pairing(n, edges):
    # find the minimum spanning tree
    mst = get_minimum_spanning_tree(n, edges)
    # calculate the maximum distance between the pairs
    max_distance = 0
    for i in range(n):
        for j in range(i+1, n):
            if find_set(i, mst) != find_set(j, mst):
                max_distance = max(max_distance, mst[i][2] + mst[j][2])
    return max_distance

def main():
    n, k = map(int, input().split())
    edges = []
    for _ in range(n-1):
        x, y = map(int, input().split())
        edges.append([x, y, 1])
    print(max_distance_pairing(n, edges))

if __name__ == '__main__':
    main()

