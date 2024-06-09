
def f1(N, barbarians):
    # Initialize a dictionary to store the words on the stone tablets
    tablets = {}
    for i in range(N):
        tablets[i+1] = barbarians[i]
    return tablets

def f2(Q, rounds, tablets):
    # Initialize a list to store the answers to Tarzan's questions
    answers = []
    for i in range(Q):
        # If the round is of type 1, show the word to the barbarians
        if rounds[i][0] == 1:
            word = rounds[i][1]
            for barbarian in tablets.values():
                if word in barbarian:
                    answers.append(1)
                    break
            else:
                answers.append(0)
        # If the round is of type 2, ask the barbarian the question
        elif rounds[i][0] == 2:
            barbarian = rounds[i][1]
            word = tablets[barbarian]
            count = 0
            for other_word in tablets.values():
                if word in other_word:
                    count += 1
            answers.append(count)
    return answers

if __name__ == '__main__':
    N = int(input())
    barbarians = [input() for _ in range(N)]
    Q = int(input())
    rounds = [input().split() for _ in range(Q)]
    tablets = f1(N, barbarians)
    answers = f2(Q, rounds, tablets)
    for answer in answers:
        print(answer)

