
def get_query_answer(string, query):
    l, r = query
    count = 0
    for i in range(l, r):
        if string[i] == ".":
            count += 1
    return count

def main():
    s = input()
    m = int(input())
    queries = []
    for i in range(m):
        queries.append(list(map(int, input().split())))
    answers = []
    for query in queries:
        answers.append(get_query_answer(s, query))
    print(*answers)

if __name__ == '__main__':
    main()

