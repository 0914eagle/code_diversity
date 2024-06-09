
import math

def get_angle(hour, minute):
    return (hour * 30 + minute / 2.0) % 360

def get_distance(hour_hand_length, minute_hand_length, hour, minute):
    angle = get_angle(hour, minute)
    return math.sin(math.radians(angle)) * hour_hand_length + math.cos(math.radians(angle)) * minute_hand_length

def main():
    hour_hand_length, minute_hand_length, hour, minute = map(int, input().split())
    print(get_distance(hour_hand_length, minute_hand_length, hour, minute))

if __name__ == '__main__':
    main()

