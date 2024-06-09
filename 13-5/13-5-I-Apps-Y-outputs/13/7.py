
def get_subsequences(s):
    subsequences = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subsequences.append(s[i:j])
    return subsequences

def get_cost(s, subsequence):
    return len(s) - len(subsequence)

def get_min_cost(s, k):
    subsequences = get_subsequences(s)
    costs = [get_cost(s, subsequence) for subsequence in subsequences]
    if len(costs) < k:
        return -1
    return sum(sorted(costs[:k])[::-1])

def main():
    n, k = map(int, input().split())
    s = input()
    print(get_min_cost(s, k))

if __name__ == '__main__':
    main()

