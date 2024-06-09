
def get_painter_time(painter_count, picture_count, painter_time):
    painter_time = sorted(painter_time, key=lambda x: x[0])
    picture_time = [0] * picture_count
    for painter in range(painter_count):
        for picture in range(picture_count):
            picture_time[picture] += painter_time[painter][picture]
    return picture_time

def get_ready_time(painter_count, picture_count, painter_time):
    picture_time = get_painter_time(painter_count, picture_count, painter_time)
    ready_time = [0] * picture_count
    for picture in range(1, picture_count):
        ready_time[picture] = ready_time[picture - 1] + picture_time[picture - 1]
    return ready_time

if __name__ == '__main__':
    painter_count, picture_count = map(int, input().split())
    painter_time = []
    for _ in range(painter_count):
        painter_time.append(list(map(int, input().split())))
    ready_time = get_ready_time(painter_count, picture_count, painter_time)
    print(*ready_time, sep='\n')

