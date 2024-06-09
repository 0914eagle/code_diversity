
def get_correct_answers(n):
    return [input() for _ in range(n)]

def get_final_score(correct_answers, student_answers):
    return sum(int(student_answers[i] == correct_answers[i]) for i in range(len(correct_answers)))

def main():
    n = int(input())
    correct_answers = get_correct_answers(n)
    student_answers = [input() for _ in range(n)]
    final_score = get_final_score(correct_answers, student_answers)
    print(final_score)

if __name__ == '__main__':
    main()

