
def get_time_difference(t1, t2):
    return abs(t1 - t2)

def get_clock_face_position(t, h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    clock_face_position = (total_seconds / 3600) % 12
    return clock_face_position

def can_prepare_contest_on_time(t1, t2, h, m, s):
    time_difference = get_time_difference(t1, t2)
    clock_face_position = get_clock_face_position(t1, h, m, s)
    if time_difference == 0:
        return "YES"
    if time_difference == 1:
        return "NO"
    if time_difference == 2:
        return "YES"
    if time_difference == 3:
        return "NO"
    if time_difference == 4:
        return "YES"
    if time_difference == 5:
        return "NO"
    if time_difference == 6:
        return "YES"
    if time_difference == 7:
        return "NO"
    if time_difference == 8:
        return "YES"
    if time_difference == 9:
        return "NO"
    if time_difference == 10:
        return "YES"
    if time_difference == 11:
        return "NO"

def main():
    h, m, s, t1, t2 = map(int, input().split())
    print(can_prepare_contest_on_time(t1, t2, h, m, s))

if __name__ == '__main__':
    main()

