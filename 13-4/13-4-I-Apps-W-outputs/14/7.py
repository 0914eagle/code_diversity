
def get_painter_time(painter_id, picture_id, time_per_unit):
    return time_per_unit[painter_id - 1][picture_id - 1]

def get_picture_time(painter_id, picture_id, time_per_unit):
    return sum(time_per_unit[painter_id - 1][:picture_id])

def get_ready_time(painter_id, picture_id, time_per_unit):
    return get_picture_time(painter_id, picture_id, time_per_unit) + get_painter_time(painter_id, picture_id, time_per_unit)

def main():
    m, n = map(int, input().split())
    time_per_unit = []
    for i in range(n):
        time_per_unit.append(list(map(int, input().split())))
    ready_times = []
    for i in range(m):
        ready_times.append(get_ready_time(n, i + 1, time_per_unit))
    print(*ready_times, sep='\n')

if __name__ == '__main__':
    main()

