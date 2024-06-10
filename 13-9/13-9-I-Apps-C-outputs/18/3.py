
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_leash_length(toy_coordinates, tree_coordinates):
    leash_length = 0
    current_toy = toy_coordinates[0]
    for tree in tree_coordinates:
        distance_to_tree = get_distance(current_toy[0], current_toy[1], tree[0], tree[1])
        if distance_to_tree > leash_length:
            leash_length = distance_to_tree
        current_toy = toy_coordinates[toy_coordinates.index(current_toy) + 1]
    return leash_length

def main():
    n, m = map(int, input().split())
    toy_coordinates = []
    for i in range(n):
        x, y = map(int, input().split())
        toy_coordinates.append((x, y))
    tree_coordinates = []
    for i in range(m):
        x, y = map(int, input().split())
        tree_coordinates.append((x, y))
    print(f"{get_leash_length(toy_coordinates, tree_coordinates):.2f}")

if __name__ == '__main__':
    main()

