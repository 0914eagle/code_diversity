
def get_possible_answers(b, d, c, l):
    answers = []
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if i + j + k == l and i * b + j * d + k * c == 14:
                    answers.append([i, j, k])
    return answers

def print_answers(answers):
    for answer in answers:
        print(f"{answer[0]} {answer[1]} {answer[2]}")

def main():
    b, d, c, l = map(int, input().split())
    answers = get_possible_answers(b, d, c, l)
    print_answers(answers)

if __name__ == '__main__':
    main()

