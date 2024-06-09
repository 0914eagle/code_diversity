
def get_correct_answers(n):
    return [input() for _ in range(n)]

def get_student_answers(n):
    return [input() for _ in range(n)]

def get_final_score(correct_answers, student_answers):
    return sum(correct_answers.index(answer) + 1 for answer in student_answers)

if __name__ == '__main__':
    n = int(input())
    correct_answers = get_correct_answers(n)
    student_answers = get_student_answers(n)
    print(get_final_score(correct_answers, student_answers))

