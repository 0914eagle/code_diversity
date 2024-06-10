
def get_correct_answers(answers):
    correct_answers = 0
    for i in range(len(answers)):
        if answers[i] == 'A':
            correct_answers += 1
    return correct_answers

def adrian_sequence(n):
    return ['A', 'B', 'C'] * (n // 3)

def bruno_sequence(n):
    return ['B', 'A', 'B', 'C'] * (n // 4)

def goran_sequence(n):
    return ['C', 'C', 'A', 'A', 'B', 'B', 'C', 'C', 'A', 'A', 'B', 'B'] * (n // 12)

def main():
    n = int(input())
    answers = input()
    adrian_correct = get_correct_answers(adrian_sequence(n))
    bruno_correct = get_correct_answers(bruno_sequence(n))
    goran_correct = get_correct_answers(goran_sequence(n))
    max_correct = max(adrian_correct, bruno_correct, goran_correct)
    if adrian_correct == max_correct:
        print("Adrian")
    if bruno_correct == max_correct:
        print("Bruno")
    if goran_correct == max_correct:
        print("Goran")

if __name__ == '__main__':
    main()

