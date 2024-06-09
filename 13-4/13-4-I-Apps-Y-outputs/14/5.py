
def get_marks(n):
    # Initialize an empty dictionary to store the marks for each student
    marks = {}
    
    # Iterate through the input and add the marks for each student to the dictionary
    for _ in range(n):
        name, *scores = input().split()
        marks[name] = list(map(int, scores))
    
    return marks

def get_average(marks, query_name):
    # Get the marks for the student with the given name
    student_marks = marks[query_name]
    
    # Calculate the average of the student's marks
    average = sum(student_marks) / len(student_marks)
    
    # Round the average to 2 decimal places
    average = round(average, 2)
    
    return average

def main():
    # Get the number of students
    n = int(input())
    
    # Get the marks for each student
    marks = get_marks(n)
    
    # Get the name of the student to query
    query_name = input()
    
    # Get the average of the student's marks
    average = get_average(marks, query_name)
    
    # Print the average
    print(average)

if __name__ == '__main__':
    main()

