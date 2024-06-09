
def get_correct_answers(answers, sequence):
    correct_answers = 0
    for i, answer in enumerate(answers):
        if answer == sequence[i % len(sequence)]:
            correct_answers += 1
    return correct_answers

def get_winner(answers, sequences):
    correct_answers = [get_correct_answers(answers, sequence) for sequence in sequences]
    max_correct_answers = max(correct_answers)
    winners = [name for i, name in enumerate(names) if correct_answers[i] == max_correct_answers]
    return max_correct_answers, sorted(winners)

names = ["Adrian", "Bruno", "Goran"]
sequences = [
    "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C",
    "B", "A", "B", "C", "B", "A", "B", "C", "B", "A", "B", "C",
    "C", "C", "A", "A", "B", "B", "C", "C", "A", "A", "B", "B"
]

answers = input()
max_correct_answers, winners = get_winner(answers, sequences)
print(max_correct_answers)
print(" ".join(winners))

