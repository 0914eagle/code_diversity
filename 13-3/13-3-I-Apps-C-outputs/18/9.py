
def get_safe_wet_plan(n, strategic_points, dry_plan):
    # Initialize a set to store the pegs that are safe to remove
    safe_to_remove = set()
    
    # Iterate through the dry plan
    for i in dry_plan:
        # If the current step is a removal, add the removed peg to the safe to remove set
        if i < 0:
            safe_to_remove.add(-i)
        # If the current step is a placement, check if the peg can be safely placed
        else:
            # If the peg can be safely placed, add it to the safe to remove set
            if can_place_peg(i, strategic_points, safe_to_remove):
                safe_to_remove.add(i)
            # If the peg cannot be safely placed, return -1
            else:
                return -1
    
    # If all pegs can be safely placed, return the safe wet plan
    return list(safe_to_remove)

def can_place_peg(i, strategic_points, safe_to_remove):
    # If the peg is already safe to remove, it can be placed
    if i in safe_to_remove:
        return True
    # If the peg is not already safe to remove, check if it has any dependencies
    for j in strategic_points[i]:
        # If the peg has a dependency and it is not safe to remove, the peg cannot be placed
        if j not in safe_to_remove:
            return False
    # If the peg has no dependencies or all dependencies are safe to remove, it can be placed
    return True

n = int(input())
strategic_points = []
for i in range(n):
    strategic_points.append(set(map(int, input().split())))
dry_plan = list(map(int, input().split()))
result = get_safe_wet_plan(n, strategic_points, dry_plan)
if result == -1:
    print(-1)
else:
    print(len(result))
    print(*result)

