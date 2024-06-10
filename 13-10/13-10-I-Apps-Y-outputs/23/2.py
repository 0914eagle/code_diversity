
def get_correct_answers(answers):
    correct_answers = 0
    for i in range(len(answers)):
        if answers[i] == "A":
            correct_answers += 1
    return correct_answers

def get_best_sequence(n):
    adrian_sequence = "A" * n + "B" * n + "C" * n
    bruno_sequence = "B" * n + "A" * n + "B" * n + "C" * n
    goran_sequence = "C" * n + "C" * n + "A" * n + "A" * n + "B" * n + "B" * n
    return max(get_correct_answers(adrian_sequence), get_correct_answers(bruno_sequence), get_correct_answers(goran_sequence))

def get_names(n):
    adrian_sequence = "A" * n + "B" * n + "C" * n
    bruno_sequence = "B" * n + "A" * n + "B" * n + "C" * n
    goran_sequence = "C" * n + "C" * n + "A" * n + "A" * n + "B" * n + "B" * n
    adrian_correct_answers = get_correct_answers(adrian_sequence)
    bruno_correct_answers = get_correct_answers(bruno_sequence)
    goran_correct_answers = get_correct_answers(goran_sequence)
    if adrian_correct_answers == bruno_correct_answers and adrian_correct_answers == goran_correct_answers:
        return "Adrian, Bruno and Goran"
    elif adrian_correct_answers == bruno_correct_answers or adrian_correct_answers == goran_correct_answers:
        return "Adrian and Bruno"
    elif bruno_correct_answers == goran_correct_answers:
        return "Bruno and Goran"
    else:
        return "Goran"

if __name__ == '__main__':
    n = int(input())
    answers = input()
    correct_answers = get_correct_answers(answers)
    best_sequence = get_best_sequence(n)
    names = get_names(n)
    print(correct_answers)
    print(names)

