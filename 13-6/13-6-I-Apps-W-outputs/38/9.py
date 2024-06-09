
def is_present(name, names):
    return name in names

def get_answer(names):
    answers = []
    for i in range(len(names)):
        if is_present(names[i], names[:i]):
            answers.append("YES")
        else:
            answers.append("NO")
    return answers

if __name__ == '__main__':
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    answers = get_answer(names)
    for answer in answers:
        print(answer)

