
def can_visit_friend(n, m, teleports):
    # Initialize a set to store the points that can be reached using teleports
    reachable_points = set([0])
    
    # Iterate through the teleports
    for teleport in teleports:
        # Get the location and limit of the teleport
        location, limit = teleport
        
        # If the teleport is located at or beyond the current point, add the limit to the set of reachable points
        if location in reachable_points:
            reachable_points.add(limit)
    
    # Return "YES" if the friend's house is reachable, otherwise return "NO"
    return "YES" if m in reachable_points else "NO"

def main():
    n, m = map(int, input().split())
    teleports = []
    for _ in range(n):
        a, b = map(int, input().split())
        teleports.append((a, b))
    print(can_visit_friend(n, m, teleports))

if __name__ == '__main__':
    main()
