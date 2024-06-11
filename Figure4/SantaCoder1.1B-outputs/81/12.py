def numerical_letter_grade(grades):
    
    if len(grades) == 0:
        return []
    else:
        return [str(round(grades[0], 2)) + '+' + str(round(grades[1], 2)) + '-' + str(round(grades[2], 2)) + '+' + str(round(grades[3], 2)) + '-' + str(round(grades[4], 2))]

