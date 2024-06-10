
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_island_connected(island1, island2):
    for tree1 in island1["trees"]:
        for tree2 in island2["trees"]:
            if get_distance(tree1["x"], tree1["y"], tree2["x"], tree2["y"]) <= island1["radius"] + island2["radius"]:
                return True
    return False

def find_shortest_path(islands):
    shortest_path = math.inf
    for i in range(len(islands)):
        for j in range(i + 1, len(islands)):
            if is_island_connected(islands[i], islands[j]):
                path = get_distance(islands[i]["x"], islands[i]["y"], islands[j]["x"], islands[j]["y"])
                if path < shortest_path:
                    shortest_path = path
    return shortest_path

def get_tunnel_length(islands, ratio):
    shortest_path = find_shortest_path(islands)
    tunnel_length = math.ceil(shortest_path / ratio)
    return tunnel_length

def main():
    n, m, k = map(int, input().split())
    islands = []
    for i in range(n):
        x, y, r = map(int, input().split())
        islands.append({"x": x, "y": y, "radius": r, "trees": []})
    for i in range(m):
        x, y, h = map(int, input().split())
        for island in islands:
            if get_distance(x, y, island["x"], island["y"]) <= island["radius"]:
                island["trees"].append({"x": x, "y": y, "height": h})
                break
    tunnel_length = get_tunnel_length(islands, k)
    print(tunnel_length)

if __name__ == '__main__':
    main()

