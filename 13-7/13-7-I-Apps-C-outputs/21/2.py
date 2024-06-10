
import math

def get_island_info(island_info):
    islands = []
    for info in island_info:
        x, y, r = map(int, info.split())
        islands.append((x, y, r))
    return islands

def get_palm_tree_info(palm_tree_info):
    palm_trees = []
    for info in palm_tree_info:
        x, y, h = map(int, info.split())
        palm_trees.append((x, y, h))
    return palm_trees

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def get_min_tunnel_length(islands, palm_trees, k):
    min_length = float('inf')
    for i in range(len(islands)):
        for j in range(i+1, len(islands)):
            island1 = islands[i]
            island2 = islands[j]
            dist = get_distance(island1[0], island1[1], island2[0], island2[1])
            if dist <= island1[2] + island2[2] + min_length:
                continue
            for tree in palm_trees:
                if tree[2] * k >= dist:
                    break
            else:
                min_length = min(min_length, dist)
    if min_length == float('inf'):
        return "impossible"
    return min_length

def main():
    n, m, k = map(int, input().split())
    island_info = [input() for _ in range(n)]
    palm_tree_info = [input() for _ in range(m)]
    islands = get_island_info(island_info)
    palm_trees = get_palm_tree_info(palm_tree_info)
    print(get_min_tunnel_length(islands, palm_trees, k))

if __name__ == '__main__':
    main()

