
def get_input():
    n = int(input())
    pairs = []
    for i in range(n):
        a, b = map(int, input().split())
        pairs.append((a, b))
    return n, pairs

def get_unique_answers(n, pairs):
    answers = []
    for i in range(n):
        a, b = pairs[i]
        for op in ["+", "-", "*"]:
            if eval(f"{a} {op} {b}") not in answers:
                answers.append(eval(f"{a} {op} {b}"))
                break
    if len(answers) == n:
        return answers
    else:
        return "impossible"

def main():
    n, pairs = get_input()
    answers = get_unique_answers(n, pairs)
    if answers == "impossible":
        print(answers)
    else:
        for i in range(n):
            a, b = pairs[i]
            for op in ["+", "-", "*"]:
                if eval(f"{a} {op} {b}") == answers[i]:
                    print(f"{a} {op} {b} = {answers[i]}")
                    break

if __name__ == '__main__':
    main()

