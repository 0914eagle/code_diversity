
def solve_query_1(x, S):
    S.append(x)
    S.sort()
    return S

def solve_query_2(S):
    if len(S) == 0:
        return 0
    else:
        max_val = max(S)
        mean = sum(S) / len(S)
        return max_val - mean

def main():
    Q = int(input())
    S = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            x = int(query[1])
            S = solve_query_1(x, S)
        else:
            print(solve_query_2(S))

if __name__ == '__main__':
    main()

