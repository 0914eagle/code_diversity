
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def find_leash_length(toy_coordinates, tree_coordinates, post_coordinates):
    leash_length = 0
    current_position = post_coordinates
    for toy in toy_coordinates:
        if distance(current_position[0], current_position[1], toy[0], toy[1]) > leash_length:
            leash_length = distance(current_position[0], current_position[1], toy[0], toy[1])
        current_position = toy
    for tree in tree_coordinates:
        if distance(current_position[0], current_position[1], tree[0], tree[1]) > leash_length:
            leash_length = distance(current_position[0], current_position[1], tree[0], tree[1])
    return round(leash_length, 2)

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
    post_coordinates = (0, 0)
    print(find_leash_length(toy_coordinates, tree_coordinates, post_coordinates))

if __name__ == '__main__':
    main()

