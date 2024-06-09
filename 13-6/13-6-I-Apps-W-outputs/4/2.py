
def solve_query(query, s):
    if query[0] == 1:
        s.add(query[1])
    else:
        max_value = max(s)
        mean = sum(s) / len(s)
        return max_value - mean

def main():
    q = int(input())
    s = set()
    for i in range(q):
        query = list(map(int, input().split()))
        print(solve_query(query, s))

if __name__ == '__main__':
    main()

