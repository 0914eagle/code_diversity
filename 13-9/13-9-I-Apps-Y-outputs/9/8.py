
def get_finished_tasks(tasks, time_limit):
    total_time = 0
    finished_tasks = 0
    for task in tasks:
        if total_time + task <= time_limit:
            finished_tasks += 1
            total_time += task
        else:
            break
    return finished_tasks

