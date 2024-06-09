
def get_correct_answers(n):
    return [input() for _ in range(n)]

def get_final_score(correct_answers):
    return sum(1 for i, answer in enumerate(correct_answers, 1) if answer == "A")

def main():
    n = int(input())
    correct_answers = get_correct_answers(n)
    final_score = get_final_score(correct_answers)
    print(final_score)

if __name__ == '__main__':
    main()

