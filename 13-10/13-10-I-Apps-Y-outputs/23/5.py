
def get_correct_answers(answers):
    correct_answers = 0
    for i in range(len(answers)):
        if answers[i] == 'A':
            correct_answers += 1
    return correct_answers

def adrian_sequence(n):
    return ['A', 'B', 'C'] * (n // 3)

def bruno_sequence(n):
    return ['B', 'A', 'C'] * (n // 3)

def goran_sequence(n):
    return ['C', 'A', 'B'] * (n // 3)

def get_max_correct_answers(n, correct_answers):
    max_correct_answers = 0
    max_correct_answers_boys = []
    for i in range(3):
        if i == 0:
            boy_sequence = adrian_sequence(n)
        elif i == 1:
            boy_sequence = bruno_sequence(n)
        else:
            boy_sequence = goran_sequence(n)
        correct_answers_boy = 0
        for j in range(n):
            if boy_sequence[j] == correct_answers[j]:
                correct_answers_boy += 1
        if correct_answers_boy > max_correct_answers:
            max_correct_answers = correct_answers_boy
            max_correct_answers_boys = [i]
        elif correct_answers_boy == max_correct_answers:
            max_correct_answers_boys.append(i)
    return max_correct_answers, max_correct_answers_boys

if __name__ == '__main__':
    n = int(input())
    correct_answers = input()
    max_correct_answers, max_correct_answers_boys = get_max_correct_answers(n, correct_answers)
    print(max_correct_answers)
    print(' '.join(sorted(max_correct_answers_boys)))

