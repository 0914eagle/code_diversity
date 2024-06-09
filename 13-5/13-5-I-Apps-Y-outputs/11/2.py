
def get_final_score(n, answers):
    score = 0
    for i in range(n):
        if answers[i] == "A":
            score += 1
    return score

def main():
    n = int(input())
    answers = []
    for i in range(n):
        answers.append(input())
    print(get_final_score(n, answers))

if __name__ == '__main__':
    main()

