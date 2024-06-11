

def numerical_letter_grade(grades):
    

    # Initialize an empty list to store the letter grades
    letter_grades = []

    # Iterate through the list of GPAs
    for gpa in grades:
        # Check if the GPA is greater than or equal to 4.0
        if gpa >= 4.0:
            letter_grade = 'A+'
        # Check if the GPA is greater than 3.7
        elif gpa > 3.7:
            letter_grade = 'A'
        # Check if the GPA is greater than 3.3
        elif gpa > 3.3:
            letter_grade = 'A-'
        # Check if the GPA is greater than or equal to 3.0
        elif gpa >= 3.0:
            letter_grade = 'B+'
        # Check if the GPA is greater than 2.7
        elif gpa > 2.7:
            letter_grade = 'B'
        # Check if the GPA is greater than 2.3
        elif gpa > 2.3:
            letter_grade = 'B-'
        # Check if the GPA is greater than or equal to 2.0
        elif gpa >= 2.0:
            letter_grade = 'C+'
        # Check if the GPA is greater than 1.7
        elif gpa > 1.7:
            letter_grade = 'C'
        # Check if the GPA is greater than 1.3
        elif gpa > 1.3:
            letter_grade = 'C-'
        # Check if the GPA is greater than or equal to 1.0
        elif gpa >= 1.0:
            letter_grade = 'D+'
        # Check if the GPA is greater than 0.7
        elif gpa > 0.7:
            letter_grade = 'D'
        # Check if the GPA is greater than or equal to 0.0
        elif gpa >= 0.0:
            letter_grade = 'D-'
        # If the GPA is less than 0.0, assign an E grade
        else:
            letter_grade = 'E
