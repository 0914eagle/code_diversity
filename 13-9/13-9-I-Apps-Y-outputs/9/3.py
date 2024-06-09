
def solve(tasks, time_limit):
    completed_tasks = 0
    time_spent = 0

    for task in tasks:
        if time_spent + task <= time_limit:
            completed_tasks += 1
            time_spent += task

    return completed_tasks

