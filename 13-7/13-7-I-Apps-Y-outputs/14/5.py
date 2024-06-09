
def solve(A, B, H, M):
    # Calculate the angle made by the hour hand
    hour_angle = (360 / 12) * H
    
    # Calculate the angle made by the minute hand
    minute_angle = (360 / 60) * M
    
    # Calculate the difference between the two angles
    angle_diff = abs(hour_angle - minute_angle)
    
    # Calculate the distance between the hands
    distance = abs(A * sin(radians(angle_diff)))
    
    return distance

