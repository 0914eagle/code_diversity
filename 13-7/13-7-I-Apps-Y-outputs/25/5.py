
def get_time_to_solve_all_problems(problem_times, drink_info):
    # Initialize a dictionary to store the time it takes to solve all problems for each drink
    drink_times = {}

    # Loop through each drink
    for drink_id, (problem_id, time_boost) in drink_info.items():
        # Initialize a variable to store the total time to solve all problems for this drink
        total_time = 0

        # Loop through each problem
        for problem_id, time in problem_times.items():
            # If the problem is the one specified in the drink info, add the time boost to the time it takes to solve the problem
            if problem_id == problem_id:
                time += time_boost

            # Add the time it takes to solve the problem to the total time
            total_time += time

        # Add the total time to the dictionary
        drink_times[drink_id] = total_time

    return drink_times

