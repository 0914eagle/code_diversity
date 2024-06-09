
def get_subsequences(s):
    subsequences = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subsequences.append(s[i:j])
    return subsequences

def get_cost(s, k):
    subsequences = get_subsequences(s)
    costs = []
    for subsequence in subsequences:
        costs.append(len(s) - len(subsequence))
    return costs[k-1] if k <= len(costs) else -1

def main():
    n, k = map(int, input().split())
    s = input()
    print(get_cost(s, k))

if __name__ == '__main__':
    main()

