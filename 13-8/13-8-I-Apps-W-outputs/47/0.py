
def get_answers(s, queries):
    answers = []
    for l, r in queries:
        count = 0
        for i in range(l, r):
            if s[i] == ".":
                count += 1
        answers.append(count)
    return answers

def main():
    s = input()
    m = int(input())
    queries = []
    for i in range(m):
        l, r = map(int, input().split())
        queries.append((l, r))
    answers = get_answers(s, queries)
    for answer in answers:
        print(answer)

if __name__ == '__main__':
    main()

