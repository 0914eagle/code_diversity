
def solve(tasks, time):
    completed_tasks = 0
    total_time = 0

    for task in tasks:
        if total_time + task <= time:
            completed_tasks += 1
            total_time += task

    return completed_tasks

