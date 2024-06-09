
def average_marks(marks, query_name):
    # Use a dictionary comprehension to convert the marks list to a dictionary
    marks_dict = {name: sum(marks) / len(marks) for name, marks in marks_dict.items()}
    # Return the average marks for the queried student
    return round(marks_dict[query_name], 2)

