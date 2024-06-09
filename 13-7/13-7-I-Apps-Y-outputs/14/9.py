
def solve(A, B, H, M):
    # Calculate the angle between the hour and minute hands
    hour_angle = (360 / 12) * H
    minute_angle = (360 / 60) * M
    angle = abs(hour_angle - minute_angle)

    # Calculate the distance between the hands
    distance = (A * math.sin(math.radians(angle))) + (B * math.sin(math.radians(angle)))

    return round(distance, 9)

