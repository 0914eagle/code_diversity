
def get_subsequences(s):
    subsequences = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subsequences.append(s[i:j])
    return subsequences

def get_cost(subsequence, s):
    return len(s) - len(subsequence)

def get_min_cost(s, k):
    subsequences = get_subsequences(s)
    costs = [get_cost(subsequence, s) for subsequence in subsequences]
    if len(costs) < k:
        return -1
    return sum(sorted(costs[:k]));

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(get_min_cost(s, k))

