
def get_subsequence(a, b):
    # Find the longest common subsequence of a and b
    # If there are multiple LCS, return any one of them
    lcs = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                lcs.append(a[i])
                break
    return lcs

def get_subsequences(a, b):
    # Find all non-empty subsequence of a and b
    # If there are multiple subsequence with the smallest possible length, return any one of them
    subseqs = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                subseqs.append([a[i]])
                break
    return subseqs

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        subseq = get_subsequence(a, b)
        if subseq:
            print("YES")
            print(len(subseq))
            print(" ".join(map(str, subseq)))
        else:
            print("NO")

if __name__ == '__main__':
    main()

