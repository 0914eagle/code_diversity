
def solve(n, T, tasks):
    total_time = 0
    count = 0
    for task in tasks:
        total_time += task
        count += 1
        if total_time > T:
            break
    return count

