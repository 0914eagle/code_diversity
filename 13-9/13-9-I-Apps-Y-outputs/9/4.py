
def solve(n, T, tasks):
    total_time = 0
    count = 0
    for task in tasks:
        if total_time + task <= T:
            total_time += task
            count += 1
        else:
            break
    return count

