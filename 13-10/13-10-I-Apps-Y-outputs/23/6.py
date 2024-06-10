
def get_correct_answers(sequence, correct_answers):
    return sum(1 for x, y in zip(sequence, correct_answers) if x == y)

def get_max_correct_answers(correct_answers):
    return max(get_correct_answers(sequence, correct_answers) for sequence in [
        "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"
    ])

def get_winners(correct_answers):
    max_correct_answers = get_max_correct_answers(correct_answers)
    return sorted(name for name, sequence in [
        ("Adrian", "A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"),
        ("Bruno", "B", "A", "B", "C", "B", "A", "B", "C", "B", "A", "B", "C"),
        ("Goran", "C", "C", "A", "A", "B", "B", "C", "C", "A", "A", "B", "B")
    ] if get_correct_answers(sequence, correct_answers) == max_correct_answers)

if __name__ == '__main__':
    correct_answers = input()
    print(get_max_correct_answers(correct_answers))
    print(*get_winners(correct_answers))

