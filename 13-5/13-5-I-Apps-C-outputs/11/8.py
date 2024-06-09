
import math
import random

def get_tree_overlap(boar_center, tree_center, boar_radius, tree_radius):
    
    dx = tree_center[0] - boar_center[0]
    dy = tree_center[1] - boar_center[1]
    distance = math.sqrt(dx**2 + dy**2)
    if distance > boar_radius + tree_radius:
        return 0
    if distance <= abs(boar_radius - tree_radius):
        return math.pi * min(boar_radius, tree_radius)**2
    angle = math.acos(min(boar_radius, distance) / boar_radius)
    sector_area = 0.5 * (angle - math.sin(angle)) * boar_radius**2
    remaining_area = math.pi * tree_radius**2 - sector_area
    return remaining_area

def get_probability(boar_center, boar_radius, tree_centers, tree_radii):
    
    total_area = 0
    for tree_center, tree_radius in zip(tree_centers, tree_radii):
        total_area += get_tree_overlap(boar_center, tree_center, boar_radius, tree_radius)
    return 1 - total_area / (math.pi * boar_radius**2)

def main():
    n = int(input())
    tree_centers = []
    tree_radii = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        tree_centers.append((x, y))
        tree_radii.append(r)
    b, d = map(int, input().split())
    boar_center = (0, 0)
    boar_radius = b
    probability = get_probability(boar_center, boar_radius, tree_centers, tree_radii)
    print(probability)

if __name__ == '__main__':
    main()

