
def get_subsequences(s):
    subsequences = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subsequences.append(s[i:j])
    return subsequences

def get_cost(s, k):
    subsequences = get_subsequences(s)
    total_cost = 0
    for subsequence in subsequences:
        if len(subsequence) == k:
            total_cost += len(s) - len(subsequence)
            break
    return total_cost

def solve(s, k):
    if k == 0:
        return 0
    if len(s) == 0:
        return -1
    cost = get_cost(s, k)
    if cost == -1:
        return -1
    return cost + solve(s[1:], k-1)

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(solve(s, k))

