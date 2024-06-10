
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_tunnel_length(islands, palm_trees, k):
    # Initialize variables
    min_length = 0
    max_length = 0
    for island in islands:
        x, y, r = island
        for palm_tree in palm_trees:
            px, py, ph = palm_tree
            distance = get_distance(x, y, px, py)
            if distance <= r:
                continue
            if distance > max_length:
                max_length = distance
    if max_length == 0:
        return 0
    return max_length * k

def main():
    n, m, k = map(int, input().split())
    islands = []
    for i in range(n):
        x, y, r = map(int, input().split())
        islands.append((x, y, r))
    palm_trees = []
    for i in range(m):
        x, y, h = map(int, input().split())
        palm_trees.append((x, y, h))
    print(get_tunnel_length(islands, palm_trees, k))

if __name__ == '__main__':
    main()

