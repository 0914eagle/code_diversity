
def get_barbarian_words(barbarians):
    return [barbarian.lower() for barbarian in barbarians]

def get_barbarian_tablets(barbarians):
    return [barbarian.lower() for barbarian in barbarians]

def get_barbarian_answers(barbarians, shown_words, questions):
    answers = []
    for question in questions:
        if question[0] == 1:
            shown_word = question[1]
            answers.append(sum(1 for word in barbarians if shown_word in word))
        else:
            barbarian_index = question[1] - 1
            answers.append(sum(1 for word in barbarians if barbarians[barbarian_index] in word))
    return answers

def main():
    num_barbarians = int(input())
    barbarians = [input() for _ in range(num_barbarians)]
    num_rounds = int(input())
    shown_words = [input() for _ in range(num_rounds)]
    questions = [[int(x) for x in input().split()] for _ in range(num_rounds)]
    answers = get_barbarian_answers(barbarians, shown_words, questions)
    for answer in answers:
        print(answer)

if __name__ == '__main__':
    main()

