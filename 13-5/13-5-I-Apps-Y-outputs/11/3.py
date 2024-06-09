
def get_correct_answers(n):
    return [input() for _ in range(n)]

def get_student_answers(n):
    return [input() for _ in range(n)]

def get_score(correct_answers, student_answers):
    score = 0
    for i, answer in enumerate(student_answers, start=1):
        if answer == correct_answers[i-1]:
            score += 1
    return score

def main():
    n = int(input())
    correct_answers = get_correct_answers(n)
    student_answers = get_student_answers(n)
    score = get_score(correct_answers, student_answers)
    print(score)

if __name__ == '__main__':
    main()

