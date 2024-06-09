
import math

def get_angle(hour, minute):
    return (hour * 30 + minute * 0.5) % 360

def get_distance(hour_angle, minute_angle, hour_hand_length, minute_hand_length):
    return math.sin(math.radians(hour_angle)) * hour_hand_length + math.sin(math.radians(minute_angle)) * minute_hand_length

def main():
    hour_hand_length, minute_hand_length, hour, minute = map(int, input().split())
    hour_angle = get_angle(hour, 0)
    minute_angle = get_angle(0, minute)
    distance = get_distance(hour_angle, minute_angle, hour_hand_length, minute_hand_length)
    print(distance)

if __name__ == '__main__':
    main()

