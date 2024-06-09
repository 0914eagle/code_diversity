
def get_marks(n):
    # Initialize an empty dictionary to store the marks for each student
    marks = {}
    
    # Iterate through the input and add the marks for each student to the dictionary
    for _ in range(n):
        name, *scores = input().split()
        marks[name] = list(map(int, scores))
    
    return marks

def get_average(marks, name):
    # Return the average of the marks for the specified student
    return sum(marks[name]) / len(marks[name])

def main():
    # Get the number of students
    n = int(input())
    
    # Get the marks for each student
    marks = get_marks(n)
    
    # Get the name of the student to query
    query_name = input()
    
    # Calculate the average of the marks for the specified student
    average = get_average(marks, query_name)
    
    # Print the average to 2 decimal places
    print(f"{average:.2f}")

if __name__ == '__main__':
    main()

