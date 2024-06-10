
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_leash_length(toys, trees):
    leash_length = 0
    current_toy = toys[0]
    while current_toy:
        # Find the closest tree
        closest_tree = None
        for tree in trees:
            if distance(current_toy[0], current_toy[1], tree[0], tree[1]) < leash_length:
                closest_tree = tree
                break
        
        # If there is no tree within leash length, Spot can go directly to the next toy
        if not closest_tree:
            leash_length += distance(current_toy[0], current_toy[1], toys[1][0], toys[1][1])
            current_toy = toys[1]
        # Otherwise, Spot has to go around the tree first
        else:
            leash_length += distance(current_toy[0], current_toy[1], closest_tree[0], closest_tree[1])
            current_toy = toys[1]
    
    return round(leash_length, 2)

def main():
    n, m = map(int, input().split())
    toys = []
    for i in range(n):
        x, y = map(int, input().split())
        toys.append([x, y])
    trees = []
    for i in range(m):
        x, y = map(int, input().split())
        trees.append([x, y])
    print(get_leash_length(toys, trees))

if __name__ == '__main__':
    main()

