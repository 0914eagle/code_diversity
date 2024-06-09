
def solve(marks, query_name):
    # Find the marks of the student with the given name
    student_marks = marks[query_name]
    # Calculate the average of the marks
    average = sum(student_marks) / len(student_marks)
    # Round the average to 2 decimal places
    average = round(average, 2)
    return average

