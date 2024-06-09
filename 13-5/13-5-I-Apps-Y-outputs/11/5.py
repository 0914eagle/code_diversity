
def get_correct_answers(n):
    return [input() for _ in range(n)]

def get_student_answers(n):
    return [input() for _ in range(n)]

def get_score(correct_answers, student_answers):
    return sum(int(student_answers[i] == correct_answers[i]) for i in range(len(correct_answers)))

def main():
    n = int(input())
    correct_answers = get_correct_answers(n)
    student_answers = get_student_answers(n)
    score = get_score(correct_answers, student_answers)
    print(score)

if __name__ == '__main__':
    main()

