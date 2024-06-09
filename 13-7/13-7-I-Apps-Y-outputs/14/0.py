
def solve(A, B, H, M):
    # Calculate the angle between the hour and minute hands
    angle = (M / 60.0) * 360
    
    # Calculate the distance between the hands at the given time
    distance = (A * math.sin(math.radians(angle))) + (B * math.sin(math.radians(angle)))
    
    return distance

