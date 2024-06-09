
def solve(marks, query_name):
    # Find the marks for the query_name
    query_marks = marks[query_name]
    # Calculate the average of the marks
    average = sum(query_marks) / len(query_marks)
    # Round the average to 2 decimal places
    average = round(average, 2)
    return average

