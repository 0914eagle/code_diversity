
import math

def calculate_leash_length(n, m, toy_coordinates, tree_coordinates):
    # Calculate the distance between the post and the first toy
    first_toy_distance = math.sqrt((toy_coordinates[0][0] - 0) ** 2 + (toy_coordinates[0][1] - 0) ** 2)

    # Calculate the distance between the post and the last toy
    last_toy_distance = math.sqrt((toy_coordinates[-1][0] - 0) ** 2 + (toy_coordinates[-1][1] - 0) ** 2)

    # Calculate the distance between the post and the first tree
    first_tree_distance = math.sqrt((tree_coordinates[0][0] - 0) ** 2 + (tree_coordinates[0][1] - 0) ** 2)

    # Calculate the distance between the post and the last tree
    last_tree_distance = math.sqrt((tree_coordinates[-1][0] - 0) ** 2 + (tree_coordinates[-1][1] - 0) ** 2)

    # Calculate the maximum distance Spot can travel between any two toys
    max_toy_distance = max(first_toy_distance, last_toy_distance)

    # Calculate the maximum distance Spot can travel between any two trees
    max_tree_distance = max(first_tree_distance, last_tree_distance)

    # Calculate the leash length needed to get to all toys and trees
    leash_length = max(max_toy_distance, max_tree_distance)

    return round(leash_length, 2)

def main():
    n, m = map(int, input().split())
    toy_coordinates = []
    tree_coordinates = []
    for i in range(n):
        x, y = map(int, input().split())
        toy_coordinates.append((x, y))
    for i in range(m):
        x, y = map(int, input().split())
        tree_coordinates.append((x, y))
    print(calculate_leash_length(n, m, toy_coordinates, tree_coordinates))

if __name__ == '__main__':
    main()

