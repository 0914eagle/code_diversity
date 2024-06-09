
def get_correct_answers(n):
    return [input() for _ in range(n)]

def get_final_score(answers):
    return sum(i for i, answer in enumerate(answers, start=1) if answer == "A")

def main():
    n = int(input())
    answers = get_correct_answers(n)
    final_score = get_final_score(answers)
    print(final_score)

if __name__ == '__main__':
    main()

