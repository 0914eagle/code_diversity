
def solve(S, x):
    S.append(x)
    S.sort()
    return S

def find_subset(S):
    max_value = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            subset = S[i:j+1]
            max_value = max(max_value, max(subset) - sum(subset) / len(subset))
    return max_value

if __name__ == '__main__':
    S = []
    queries = int(input())
    for _ in range(queries):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            S = solve(S, x)
        else:
            print(find_subset(S))

