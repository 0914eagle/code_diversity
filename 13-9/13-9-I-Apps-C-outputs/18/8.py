
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def find_longest_distance(toys, trees):
    longest_distance = 0
    for i in range(len(toys)):
        for j in range(i+1, len(toys)):
            toy1 = toys[i]
            toy2 = toys[j]
            distance = calculate_distance(toy1[0], toy1[1], toy2[0], toy2[1])
            if distance > longest_distance:
                longest_distance = distance
    for tree in trees:
        for toy in toys:
            distance = calculate_distance(tree[0], tree[1], toy[0], toy[1])
            if distance > longest_distance:
                longest_distance = distance
    return longest_distance

def main():
    n, m = map(int, input().split())
    toys = []
    for i in range(n):
        x, y = map(int, input().split())
        toys.append((x, y))
    trees = []
    for i in range(m):
        x, y = map(int, input().split())
        trees.append((x, y))
    print(round(find_longest_distance(toys, trees), 2))

if __name__ == '__main__':
    main()

