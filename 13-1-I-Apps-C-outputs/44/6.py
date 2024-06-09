
import math
import random

def solve(n, trees, b, d):
    # Calculate the total area of the forest
    total_area = 0
    for tree in trees:
        total_area += math.pi * tree[2] ** 2
    
    # Calculate the probability of the boar hitting a tree
    prob_hit = 0
    for tree in trees:
        # Calculate the distance between the boar and the tree
        dist = math.sqrt((tree[0] - b) ** 2 + (tree[1] - b) ** 2)
        
        # Calculate the area of overlap between the boar and the tree
        overlap = math.pi * min(dist, b + tree[2]) ** 2
        
        # Add the probability of hitting the tree to the total probability
        prob_hit += overlap / total_area
    
    # Calculate the probability of completing the charge without hitting a tree
    prob_complete = 1 - prob_hit
    
    return prob_complete

n = int(input())
trees = []
for i in range(n):
    x, y, r = map(int, input().split())
    trees.append([x, y, r])
b, d = map(int, input().split())

print(solve(n, trees, b, d))
