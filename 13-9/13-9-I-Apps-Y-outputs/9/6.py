
def get_completed_tasks(tasks, time_limit):
    total_time = 0
    completed_tasks = 0
    for task in tasks:
        if total_time + task <= time_limit:
            total_time += task
            completed_tasks += 1
    return completed_tasks

