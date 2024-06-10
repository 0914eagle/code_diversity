
def get_valid_scenarios(n, questions):
    valid_scenarios = set()
    for i in range(n):
        for j in range(i+1, n+1):
            if j-i <= 1:
                continue
            valid_scenarios.add((i, j))
    return valid_scenarios

def count_scenarios(n, questions, valid_scenarios):
    count = 0
    for i in range(len(questions)):
        question = questions[i]
        for j in range(i+1, len(questions)):
            next_question = questions[j]
            if question == next_question:
                continue
            for scenario in valid_scenarios:
                if scenario[0] == question and scenario[1] == next_question:
                    count += 1
                    break
    return count

def main():
    n, k = map(int, input().split())
    questions = list(map(int, input().split()))
    valid_scenarios = get_valid_scenarios(n, questions)
    count = count_scenarios(n, questions, valid_scenarios)
    print(count)

if __name__ == '__main__':
    main()

