
def get_substring_count(s, l, r):
    count = 0
    for i in range(l, r):
        if s[i] == ".":
            count += 1
    return count

def solve(s, queries):
    result = []
    for query in queries:
        l, r = query
        result.append(get_substring_count(s, l, r))
    return result

def main():
    s = input()
    m = int(input())
    queries = []
    for i in range(m):
        l, r = map(int, input().split())
        queries.append((l, r))
    result = solve(s, queries)
    for i in result:
        print(i)

if __name__ == '__main__':
    main()

