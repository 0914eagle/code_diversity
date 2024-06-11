def numerical_letter_grade(grades):
    
    # TODO: Write your solution here
    result = []
    for grade in grades:
        if grade >= 4.0:
            result.append('A+')
        elif grade >= 3.7:
            result.append('A')
        elif grade >= 3.3:
            result.append('A-')
        elif grade >= 3.0:
            result.append('B+')
        elif grade >= 2.7:
            result.append('B')
        elif grade >= 2.3:
            result.append('B-')
        elif grade >= 2.0:
            result.append('C+')
        elif grade >= 1.7:
            result.append('C')
        elif grade >= 1.3:
            result.append('C-')
        elif grade >= 1.0:
            result.append('D+')
        elif grade >= 0.7:
            result.append('D')
        elif grade >= 0.0:
            result.append('D-')
        else:
            result.append('E')
    return result


if __name__ == '__main__':
    print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))
