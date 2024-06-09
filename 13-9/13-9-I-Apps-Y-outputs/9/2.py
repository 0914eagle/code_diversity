
def tasks_completed(tasks, T):
    total_time = 0
    count = 0
    for task in tasks:
        total_time += task
        count += 1
        if total_time > T:
            return count - 1
    return count

