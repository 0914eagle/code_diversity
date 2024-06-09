
def solve(x, y, z, t1, t2, t3):
    # Calculate the time it takes to use the stairs
    time_stairs = abs(x - y) * t1
    
    # Calculate the time it takes to use the elevator
    time_elevator = t3 + t2 * abs(z - y) + t3
    
    # Check if the time it takes to use the elevator is less than the time it takes to use the stairs
    if time_elevator < time_stairs:
        return "YES"
    else:
        return "NO"

