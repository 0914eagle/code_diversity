
def get_min_turns(intersections, alice_start, bob_start):
    # Initialize a dictionary to store the distances from each intersection to the leaning tower
    tower_distances = {}
    for i in range(len(intersections)):
        tower_distances[i] = intersections[i][2]
    
    # Initialize a queue to store the intersections to visit
    queue = []
    
    # Initialize the starting intersection for Alice and Bob
    alice_curr = alice_start
    bob_curr = bob_start
    
    # Initialize the minimum number of turns it takes to show either person correct
    min_turns = 0
    
    # Loop until we find a intersection where Alice and Bob have different distances to the leaning tower
    while alice_curr != bob_curr:
        # Get the distances to the leaning tower from the current intersection for Alice and Bob
        alice_tower_dist = tower_distances[alice_curr]
        bob_tower_dist = tower_distances[bob_curr]
        
        # If Alice and Bob have the same distance to the leaning tower, we need to find the next intersection where their distances differ
        if alice_tower_dist == bob_tower_dist:
            # Add the current intersection to the queue
            queue.append(alice_curr)
            
            # Get the left and right intersections from the current intersection
            left = intersections[alice_curr][0]
            right = intersections[alice_curr][1]
            
            # If the left intersection has a shorter distance to the leaning tower than the current intersection, set the current intersection to the left intersection
            if tower_distances[left] < tower_distances[alice_curr]:
                alice_curr = left
            # Otherwise, set the current intersection to the right intersection
            else:
                alice_curr = right
            
            # If the right intersection has a shorter distance to the leaning tower than the current intersection, set the current intersection to the right intersection
            if tower_distances[right] < tower_distances[bob_curr]:
                bob_curr = right
            # Otherwise, set the current intersection to the left intersection
            else:
                bob_curr = left
            
            # Increment the minimum number of turns it takes to show either person correct
            min_turns += 1
        
        # If Alice and Bob have different distances to the leaning tower, we have found the intersection where their distances differ
        else:
            # Return the minimum number of turns it takes to show either person correct
            return min_turns
    
    # If we reach this point, Alice and Bob are at the same intersection and have the same distance to the leaning tower
    return "indistinguishable"

def main():
    # Read the number of intersections, Alice's starting intersection, and Bob's starting intersection from stdin
    n, alice_start, bob_start = map(int, input().split())
    
    # Read the intersections from stdin
    intersections = []
    for i in range(n):
        intersections.append(list(map(int, input().split())))
    
    # Call the get_min_turns function and print the result
    print(get_min_turns(intersections, alice_start, bob_start))

if __name__ == '__main__':
    main()

