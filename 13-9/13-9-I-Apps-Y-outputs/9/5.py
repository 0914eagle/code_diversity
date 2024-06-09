
def solve(n, T, tasks):
    completed_tasks = 0
    time_taken = 0

    for task in tasks:
        if time_taken + task <= T:
            completed_tasks += 1
            time_taken += task
        else:
            break

    return completed_tasks

