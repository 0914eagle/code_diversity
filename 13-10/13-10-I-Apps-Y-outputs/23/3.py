
def get_correct_answers(correct_answers, adrian_sequence, bruno_sequence, goran_sequence):
    adrian_score = 0
    bruno_score = 0
    goran_score = 0
    for i in range(len(correct_answers)):
        if correct_answers[i] == adrian_sequence[i]:
            adrian_score += 1
        if correct_answers[i] == bruno_sequence[i]:
            bruno_score += 1
        if correct_answers[i] == goran_sequence[i]:
            goran_score += 1
    return adrian_score, bruno_score, goran_score

def get_winner(correct_answers, adrian_sequence, bruno_sequence, goran_sequence):
    adrian_score, bruno_score, goran_score = get_correct_answers(correct_answers, adrian_sequence, bruno_sequence, goran_sequence)
    winner = ""
    if adrian_score == bruno_score and adrian_score == goran_score:
        winner = "All"
    elif adrian_score == bruno_score or adrian_score == goran_score:
        if adrian_score > bruno_score and adrian_score > goran_score:
            winner = "Adrian"
        elif bruno_score > adrian_score and bruno_score > goran_score:
            winner = "Bruno"
        else:
            winner = "Goran"
    else:
        if adrian_score > bruno_score and adrian_score > goran_score:
            winner = "Adrian"
        elif bruno_score > adrian_score and bruno_score > goran_score:
            winner = "Bruno"
        else:
            winner = "Goran"
    return winner

def main():
    correct_answers = input("Enter the correct answers: ").upper()
    adrian_sequence = "ABCABCABCABCABC"
    bruno_sequence = "BACBACBACBACBAC"
    goran_sequence = "CCAAAABBCCAAAABB"
    winner = get_winner(correct_answers, adrian_sequence, bruno_sequence, goran_sequence)
    print(f"The winner is: {winner}")

if __name__ == '__main__':
    main()

