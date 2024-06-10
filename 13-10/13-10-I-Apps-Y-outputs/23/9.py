
def get_correct_answers(answers, adrian_sequence, bruno_sequence, goran_sequence):
    correct_answers_adrian = 0
    correct_answers_bruno = 0
    correct_answers_goran = 0

    for i in range(len(answers)):
        if answers[i] == adrian_sequence[i % len(adrian_sequence)]:
            correct_answers_adrian += 1
        if answers[i] == bruno_sequence[i % len(bruno_sequence)]:
            correct_answers_bruno += 1
        if answers[i] == goran_sequence[i % len(goran_sequence)]:
            correct_answers_goran += 1

    return correct_answers_adrian, correct_answers_bruno, correct_answers_goran

def get_winner(correct_answers_adrian, correct_answers_bruno, correct_answers_goran):
    max_correct_answers = max(correct_answers_adrian, correct_answers_bruno, correct_answers_goran)
    if correct_answers_adrian == max_correct_answers:
        return "Adrian"
    elif correct_answers_bruno == max_correct_answers:
        return "Bruno"
    else:
        return "Goran"

def main():
    n = int(input())
    answers = input()
    adrian_sequence = "ABACABACABACABAC"
    bruno_sequence = "BABABCABABCABAB"
    goran_sequence = "CCAACACAAACAACA"
    correct_answers_adrian, correct_answers_bruno, correct_answers_goran = get_correct_answers(answers, adrian_sequence, bruno_sequence, goran_sequence)
    winner = get_winner(correct_answers_adrian, correct_answers_bruno, correct_answers_goran)
    print(correct_answers_adrian)
    print(winner)

if __name__ == '__main__':
    main()

