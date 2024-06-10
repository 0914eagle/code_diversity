
def get_clock_angle(hour, minute, second):
    angle = (hour * 30) + (minute * 0.5)
    return angle

def get_hand_distance(angle1, angle2):
    distance = abs(angle1 - angle2)
    if distance > 180:
        distance = 360 - distance
    return distance

def can_prepare_contest(hour, minute, second, t1, t2):
    clock_angle = get_clock_angle(hour, minute, second)
    hand_distance = get_hand_distance(clock_angle, t1)
    if hand_distance == 0:
        return "YES"
    hand_distance += get_hand_distance(clock_angle, t2)
    if hand_distance == 0:
        return "YES"
    return "NO"

def main():
    hour, minute, second, t1, t2 = map(int, input().split())
    print(can_prepare_contest(hour, minute, second, t1, t2))

if __name__ == '__main__':
    main()

