
def get_correct_answers(correct_answers, adrian_sequence, bruno_sequence, goran_sequence):
    adrian_correct = 0
    bruno_correct = 0
    goran_correct = 0
    for i in range(len(correct_answers)):
        if correct_answers[i] == adrian_sequence[i]:
            adrian_correct += 1
        if correct_answers[i] == bruno_sequence[i]:
            bruno_correct += 1
        if correct_answers[i] == goran_sequence[i]:
            goran_correct += 1
    return adrian_correct, bruno_correct, goran_correct

def get_winner(adrian_correct, bruno_correct, goran_correct):
    winner = ""
    if adrian_correct == bruno_correct and adrian_correct == goran_correct:
        winner = "Adrian, Bruno, and Goran"
    elif adrian_correct == bruno_correct and adrian_correct > goran_correct:
        winner = "Adrian and Bruno"
    elif adrian_correct == goran_correct and adrian_correct > bruno_correct:
        winner = "Adrian and Goran"
    elif bruno_correct == goran_correct and bruno_correct > adrian_correct:
        winner = "Bruno and Goran"
    else:
        winner = "Adrian"
    return winner

def main():
    correct_answers = input("Enter the correct answers: ")
    adrian_sequence = "ABC"
    bruno_sequence = "BAC"
    goran_sequence = "CAB"
    adrian_correct, bruno_correct, goran_correct = get_correct_answers(correct_answers, adrian_sequence, bruno_sequence, goran_sequence)
    winner = get_winner(adrian_correct, bruno_correct, goran_correct)
    print(f"The winner is {winner}")

if __name__ == '__main__':
    main()

