
def find_correct_answers(exam_answers, adrian_sequence, bruno_sequence, goran_sequence):
    correct_answers = 0
    for i in range(len(exam_answers)):
        if exam_answers[i] == adrian_sequence[i % len(adrian_sequence)]:
            correct_answers += 1
        if exam_answers[i] == bruno_sequence[i % len(bruno_sequence)]:
            correct_answers += 1
        if exam_answers[i] == goran_sequence[i % len(goran_sequence)]:
            correct_answers += 1
    return correct_answers

def find_winners(exam_answers, adrian_sequence, bruno_sequence, goran_sequence):
    correct_answers = find_correct_answers(exam_answers, adrian_sequence, bruno_sequence, goran_sequence)
    winners = []
    if correct_answers == len(adrian_sequence):
        winners.append("Adrian")
    if correct_answers == len(bruno_sequence):
        winners.append("Bruno")
    if correct_answers == len(goran_sequence):
        winners.append("Goran")
    return " ".join(sorted(winners))

if __name__ == '__main__':
    n = int(input())
    exam_answers = input()
    adrian_sequence = "ABC"
    bruno_sequence = "BAC"
    goran_sequence = "CCAB"
    print(find_correct_answers(exam_answers, adrian_sequence, bruno_sequence, goran_sequence))
    print(find_winners(exam_answers, adrian_sequence, bruno_sequence, goran_sequence))

