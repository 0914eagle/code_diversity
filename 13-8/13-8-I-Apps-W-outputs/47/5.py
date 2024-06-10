
def get_query_answer(s, l, r):
    count = 0
    for i in range(l, r):
        if s[i] == ".":
            count += 1
    return count

def solve(s, queries):
    answers = []
    for query in queries:
        l, r = query
        answers.append(get_query_answer(s, l, r))
    return answers

def main():
    s = input()
    queries = []
    for _ in range(int(input())):
        queries.append(list(map(int, input().split())))
    answers = solve(s, queries)
    for answer in answers:
        print(answer)

if __name__ == '__main__':
    main()

