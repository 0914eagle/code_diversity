
def can_visit_friend(n, m, teleports):
    # Initialize a set to store the points that can be reached using teleports
    reachable_points = set([0])
    
    # Iterate through the teleports
    for teleport in teleports:
        # Check if the teleport's location is in the set of reachable points
        if teleport[0] in reachable_points:
            # Add the teleport's limit to the set of reachable points
            reachable_points.add(teleport[1])
    
    # Check if the friend's house is in the set of reachable points
    if m in reachable_points:
        return "YES"
    else:
        return "NO"

def main():
    n, m = map(int, input().split())
    teleports = []
    for i in range(n):
        a, b = map(int, input().split())
        teleports.append((a, b))
    print(can_visit_friend(n, m, teleports))

if __name__ == '__main__':
    main()

