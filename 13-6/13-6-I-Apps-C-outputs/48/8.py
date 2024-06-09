
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
        # If the round is of the first type, show the word to Tarzan
        if rounds[i][0] == 1:
            answers.append(rounds[i][1])
        # If the round is of the second type, count the number of words on the stone tablets that have the shown word as a consecutive substring
        else:
            count = 0
            for j in range(1, N+1):
                if rounds[i][1] in tablets[j]:
                    count += 1
            answers.append(count)
    return answers

if __name__ == '__main__':
    N = int(input())
    barbarians = []
    for i in range(N):
        barbarians.append(input())
    Q = int(input())
    rounds = []
    for i in range(Q):
        rounds.append(list(map(int, input().split())))
    tablets = f1(N, barbarians)
    answers = f2(Q, rounds, tablets)
    for answer in answers:
        print(answer)

