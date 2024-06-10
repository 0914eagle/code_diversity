
def count_dots(s, l, r):
    count = 0
    for i in range(l, r):
        if s[i] == ".":
            count += 1
    return count

def solve(s, queries):
    result = []
    for query in queries:
        l, r = query
        result.append(count_dots(s, l, r))
    return result

def main():
    s = input()
    m = int(input())
    queries = []
    for i in range(m):
        queries.append(list(map(int, input().split())))
    result = solve(s, queries)
    print(*result, sep='\n')

if __name__ == '__main__':
    main()

