
def get_unique_names(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names

def get_answer(names):
    unique_names = get_unique_names(names)
    answer = []
    for name in names:
        if name in unique_names:
            answer.append("NO")
        else:
            answer.append("YES")
    return answer

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    answer = get_answer(names)
    for a in answer:
        print(a)

if __name__ == '__main__':
    main()

