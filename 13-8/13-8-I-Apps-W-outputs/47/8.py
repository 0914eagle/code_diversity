
def get_number_of_dots_between(s, l, r):
    count = 0
    for i in range(l, r):
        if s[i] == ".":
            count += 1
    return count

def solve(s, queries):
    results = []
    for query in queries:
        l, r = query
        results.append(get_number_of_dots_between(s, l, r))
    return results

def main():
    s = input()
    m = int(input())
    queries = []
    for i in range(m):
        queries.append(list(map(int, input().split())))
    results = solve(s, queries)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()

