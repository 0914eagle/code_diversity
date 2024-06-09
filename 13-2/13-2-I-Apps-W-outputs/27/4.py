
def solve(x, y, z, t1, t2, t3):
    # Calculate the time it takes to walk by the stairs
    time_by_stairs = abs(x - y) * t1
    
    # Calculate the time it takes to use the elevator
    time_by_elevator = t3 + t2 * abs(z - x) + t3 + t2 * abs(y - z) + t3
    
    # Check if the time by stairs is less than the time by elevator
    if time_by_stairs < time_by_elevator:
        return "YES"
    else:
        return "NO"

