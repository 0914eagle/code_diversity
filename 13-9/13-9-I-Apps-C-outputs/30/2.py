
def get_time(h, m, s):
    return h * 3600 + m * 60 + s

def get_angle(time1, time2):
    return (time2 - time1) * 30

def can_prepare_contest(h, m, s, t_1, t_2):
    time1 = get_time(h, m, s)
    time2 = get_time(t_1, t_2, 0)
    angle = get_angle(time1, time2)
    return angle % 360 == 0

def main():
    h, m, s, t_1, t_2 = map(int, input().split())
    print("YES" if can_prepare_contest(h, m, s, t_1, t_2) else "NO")

if __name__ == '__main__':
    main()

