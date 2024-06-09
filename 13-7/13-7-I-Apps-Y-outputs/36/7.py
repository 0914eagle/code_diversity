
def average_marks(marks, query_name):
    # Find the marks for the query_name
    marks_for_query_name = marks[query_name]

    # Calculate the average of the marks
    average = sum(marks_for_query_name) / len(marks_for_query_name)

    # Round the average to 2 decimal places
    average = round(average, 2)

    return average

