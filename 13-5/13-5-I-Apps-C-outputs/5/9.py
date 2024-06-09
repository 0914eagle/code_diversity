
def get_shortcut_time(level, shortcut_item, completion_time):
    return completion_time

def get_regular_time(level, item, completion_times):
    return completion_times[item]

def get_min_time(levels, shortcut_item, completion_times):
    min_time = 0
    for level in levels:
        if level == shortcut_item:
            min_time += get_shortcut_time(level, shortcut_item, completion_times[level])
        else:
            min_time += get_regular_time(level, shortcut_item, completion_times)
    return min_time

if __name__ == '__main__':
    n = int(input())
    levels = [int(input()) for _ in range(n)]
    shortcut_item, completion_times = {}, {}
    for level in levels:
        shortcut_item[level], completion_times[level] = map(int, input().split())
    print(get_min_time(levels, shortcut_item, completion_times))

