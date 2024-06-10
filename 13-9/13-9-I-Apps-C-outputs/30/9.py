
def get_time_difference(t_1, t_2):
    return abs(t_1 - t_2)

def get_shortest_path(t_1, t_2):
    difference = get_time_difference(t_1, t_2)
    if difference <= 6:
        return difference
    else:
        return 12 - difference

def can_prepare_contest_on_time(h, m, s, t_1, t_2):
    total_time_1 = h * 3600 + m * 60 + s
    total_time_2 = t_1 * 3600 + t_2 * 60
    difference = get_time_difference(total_time_1, total_time_2)
    shortest_path = get_shortest_path(t_1, t_2)
    if difference <= shortest_path:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    h, m, s, t_1, t_2 = map(int, input().split())
    print(can_prepare_contest_on_time(h, m, s, t_1, t_2))

