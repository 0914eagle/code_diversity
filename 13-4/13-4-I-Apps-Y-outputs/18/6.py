
import math

def get_distance(A, B, H, M):
    # Calculate the angle made by the hour and minute hands
    hour_angle = (30 * H) % 360
    minute_angle = (6 * M) % 360
    angle = abs(hour_angle - minute_angle)
    
    # Calculate the distance between the hands
    distance = math.sin(math.radians(angle)) * (A + B)
    
    return distance

def main():
    A, B, H, M = map(int, input().split())
    print(get_distance(A, B, H, M))

if __name__ == '__main__':
    main()

