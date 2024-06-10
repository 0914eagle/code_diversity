
def get_time_diff(t1, t2):
    return abs(t1 - t2)

def get_hand_angle(h, m, s):
    return (h * 30 + m) / 180 * math.pi

def get_distance_to_hand(h1, m1, s1, h2, m2, s2):
    angle1 = get_hand_angle(h1, m1, s1)
    angle2 = get_hand_angle(h2, m2, s2)
    return abs(angle1 - angle2)

def can_prepare_contest_on_time(h, m, s, t1, t2):
    time_diff = get_time_diff(t1, t2)
    if time_diff == 0:
        return "YES"
    
    for i in range(1, 13):
        if i == t1 or i == t2:
            continue
        dist = get_distance_to_hand(h, m, s, i, 0, 0)
        if dist < time_diff:
            return "NO"
    
    return "YES"

def main():
    h, m, s, t1, t2 = map(int, input().split())
    print(can_prepare_contest_on_time(h, m, s, t1, t2))

if __name__ == '__main__':
    main()

