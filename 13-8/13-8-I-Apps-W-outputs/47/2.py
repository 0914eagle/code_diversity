
def get_answer(string, l, r):
    count = 0
    for i in range(l, r):
        if string[i] == ".":
            count += 1
    return count

def solve(s, queries):
    result = []
    for query in queries:
        l, r = query
        result.append(get_answer(s, l, r))
    return result

if __name__ == '__main__':
    s = input()
    queries = []
    for _ in range(int(input())):
        queries.append(list(map(int, input().split())))
    result = solve(s, queries)
    for x in result:
        print(x)

