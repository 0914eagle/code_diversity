
import math

def get_squared_distance(r1, s1, r2, s2):
    return (r1-r2)**2 + (s1-s2)**2

def get_squared_distance_to_nearest_tree(fall_location, tree_locations):
    min_distance = math.inf
    for tree_location in tree_locations:
        distance = get_squared_distance(fall_location[0], fall_location[1], tree_location[0], tree_location[1])
        if distance < min_distance:
            min_distance = distance
    return min_distance

def solve(fall_locations, tree_locations):
    return [get_squared_distance_to_nearest_tree(fall_location, tree_locations) for fall_location in fall_locations]

