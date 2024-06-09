
def get_correct_answers(n):
    return [input() for _ in range(n)]

def get_final_score(answers):
    return sum(1 for i, answer in enumerate(answers, 1) if answer == "A")

def main():
    n = int(input())
    answers = get_correct_answers(n)
    print(get_final_score(answers))

if __name__ == '__main__':
    main()

