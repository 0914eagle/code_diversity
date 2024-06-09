
def solve(n, m, exams):
    # Sort the exams by the day they are given
    exams.sort(key=lambda x: x[0])
    
    # Initialize the schedule as a list of zeros
    schedule = [0] * n
    
    # Iterate through the exams
    for i, exam in enumerate(exams):
        # Get the day the questions are given and the day of the exam
        given_day, exam_day = exam[0], exam[1]
        
        # Check if the exam can be prepared and passed in the given day
        if given_day == exam_day:
            # If the exam can be prepared and passed in the given day, add it to the schedule
            schedule[given_day - 1] = i + 1
        else:
            # If the exam cannot be prepared and passed in the given day, check if it can be prepared in the previous day
            if schedule[given_day - 2] == 0:
                # If the exam can be prepared in the previous day, add it to the schedule
                schedule[given_day - 2] = i + 1
            else:
                # If the exam cannot be prepared in the previous day, return -1 as the schedule is impossible
                return -1
    
    # Return the schedule
    return schedule

