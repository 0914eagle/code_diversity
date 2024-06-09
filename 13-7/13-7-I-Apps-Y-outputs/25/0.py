
def get_solve_time(problem_times, drink_info):
    drink_map = {}
    for drink, problem, time in drink_info:
        drink_map[drink] = problem_times[:]
        drink_map[drink][problem-1] = time
    return [sum(problem_times) for problem_times in drink_map.values()]

