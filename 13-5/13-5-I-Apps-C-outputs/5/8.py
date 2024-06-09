
def get_shortcut_time(level, shortcut, completion_time):
    return completion_time

def get_rule_time(level, item, completion_time):
    return completion_time

def get_min_time(levels):
    min_time = 0
    for level in levels:
        shortcut, completion_time = level[0], level[1]
        item, completion_time = level[2], level[3]
        min_time += get_shortcut_time(level, shortcut, completion_time)
        min_time += get_rule_time(level, item, completion_time)
    return min_time

if __name__ == '__main__':
    levels = [[1, 1, 40, 30, 20, 10], [3, 1, 95, 95, 95, 10], [2, 1, 95, 50, 30, 20]]
    print(get_min_time(levels))

