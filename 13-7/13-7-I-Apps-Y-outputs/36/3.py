
def average_marks(marks, query_name):
    # Find the average of the marks array for the query_name
    average = sum(marks[query_name]) / len(marks[query_name])
    
    # Round the average to 2 decimal places
    average = round(average, 2)
    
    return average

