
def get_intersection_map(n, edges):
    # Create a dictionary to store the intersection map
    intersection_map = {}
    
    # Iterate over the edges and add them to the dictionary
    for edge in edges:
        intersection_map[edge[0]] = edge[1:]
    
    return intersection_map

def get_visible_intersections(n, tower_locations):
    # Create a set to store the visible intersections
    visible_intersections = set()
    
    # Iterate over the tower locations and add them to the set
    for tower_location in tower_locations:
        visible_intersections.add(tower_location)
    
    return visible_intersections

def get_min_turns(starting_point, intersection_map, visible_intersections):
    # Initialize the number of turns to 0
    num_turns = 0
    
    # Initialize the current intersection to the starting point
    current_intersection = starting_point
    
    # Iterate until we reach an intersection that is visible for both Alice and Bob
    while current_intersection not in visible_intersections:
        # Get the left and right intersections for the current intersection
        left_intersection, right_intersection = intersection_map[current_intersection]
        
        # Add a turn to the number of turns
        num_turns += 1
        
        # Set the current intersection to the left or right intersection based on the direction taken
        current_intersection = left_intersection if current_intersection == starting_point else right_intersection
    
    return num_turns

def main():
    # Read the number of intersections and the starting points from stdin
    n, alice_start, bob_start = map(int, input().split())
    
    # Read the edges and tower locations from stdin
    edges = [tuple(map(int, input().split())) for _ in range(n)]
    tower_locations = set(map(int, input().split()))
    
    # Create the intersection map and the set of visible intersections
    intersection_map = get_intersection_map(n, edges)
    visible_intersections = get_visible_intersections(n, tower_locations)
    
    # Get the minimum number of turns for Alice and Bob
    alice_min_turns = get_min_turns(alice_start, intersection_map, visible_intersections)
    bob_min_turns = get_min_turns(bob_start, intersection_map, visible_intersections)
    
    # Check if Alice and Bob have the same minimum number of turns
    if alice_min_turns == bob_min_turns:
        print("indistinguishable")
    else:
        print(min(alice_min_turns, bob_min_turns))

if __name__ == '__main__':
    main()

