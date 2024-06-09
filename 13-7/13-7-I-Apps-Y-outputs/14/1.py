
import math

def solve(A, B, H, M):
    # Calculate the angle made by the hour and minute hands
    hour_angle = (360 / 12) * H
    minute_angle = (360 / 60) * M
    total_angle = abs(hour_angle - minute_angle)

    # Calculate the distance between the hands
    distance = abs(A * math.sin(math.radians(total_angle / 2)))

    return distance

