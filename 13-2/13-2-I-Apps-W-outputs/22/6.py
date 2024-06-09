
def get_maximum_students_with_favorite_drink(n, k, a):
    # Initialize variables
    max_students = 0
    current_students = 0
    current_drinks = []
    
    # Iterate through the students
    for i in range(n):
        # If the current student has a favorite drink that is not in the current drinks, add it to the current drinks
        if a[i] not in current_drinks:
            current_drinks.append(a[i])
            current_students += 1
        
        # If the current students have the maximum number of drinks, update the maximum number of students
        if current_students == k:
            max_students = max(max_students, current_students)
            current_students = 0
            current_drinks = []
    
    # If there are any students left, add them to the current students
    if current_students > 0:
        max_students = max(max_students, current_students)
    
    return max_students

