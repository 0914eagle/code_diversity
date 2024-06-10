
def get_possible_answers(b, d, c, l):
    answers = []
    for i in range(1, min(b, d, c) + 1):
        for j in range(1, min(b, d, c) + 1):
            for k in range(1, min(b, d, c) + 1):
                if i + j + k == l and i * b + j * d + k * c == l:
                    answers.append([i, j, k])
    return sorted(answers)

def double_check_answers(answers):
    for answer in answers:
        if answer[0] + answer[1] + answer[2] != 14:
            return False
    return True

if __name__ == '__main__':
    b, d, c, l = map(int, input().split())
    answers = get_possible_answers(b, d, c, l)
    if double_check_answers(answers):
        for answer in answers:
            print(f"{answer[0]} {answer[1]} {answer[2]}")
    else:
        print("impossible")

