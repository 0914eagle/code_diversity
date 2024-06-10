
def get_answers(b, d, c, l):
    answers = []
    for i in range(1, min(b, d, c) + 1):
        for j in range(1, min(b - i, d, c) + 1):
            for k in range(1, min(b - i - j, d - j, c - k) + 1):
                if i + j + k == l:
                    answers.append([i, j, k])
    return sorted(answers)

def check_answers(answers, b, d, c, l):
    for answer in answers:
        if answer[0] * b + answer[1] * d + answer[2] * c == l:
            return True
    return False

if __name__ == '__main__':
    b, d, c, l = map(int, input().split())
    answers = get_answers(b, d, c, l)
    if check_answers(answers, b, d, c, l):
        for answer in answers:
            print(*answer)
    else:
        print("impossible")

