def numerical_letter_grade(grades):
    
    # Your code here
    return [str(round(grades[i] + 0.05, 1)) for i in range(len(grades))]


