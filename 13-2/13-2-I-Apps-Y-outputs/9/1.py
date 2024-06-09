
def get_cleanup_phases(days):
    dirtiness = 0
    cleanup_phases = 0
    for day in days:
        dirtiness += 1
        if dirtiness > 20:
            cleanup_phases += 1
            dirtiness = 0
    return cleanup_phases

if __name__ == '__main__':
    num_dirty_pushes = int(input())
    days = [int(x) for x in input().split()]
    print(get_cleanup_phases(days))

