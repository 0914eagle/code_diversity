
def solve(L, v, l, r):
    # Calculate the number of lanterns visible
    num_lanterns = L // v
    
    # Subtract the number of lanterns covered by the standing train
    num_lanterns -= (r - l + 1) // v
    
    return num_lanterns

