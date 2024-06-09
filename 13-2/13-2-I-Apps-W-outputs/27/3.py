
def solve(x, y, z, t1, t2, t3):
    # Calculate the time it takes to walk up by the stairs
    time_by_stairs = abs(x - y) * t1
    
    # Calculate the time it takes to use the elevator
    time_by_elevator = t3 + t2 * abs(z - y) + t3
    
    # Check if the time it takes to use the elevator is less than the time it takes to walk up by the stairs
    if time_by_elevator < time_by_stairs:
        return "YES"
    else:
        return "NO"

