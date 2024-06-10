
def get_subsequence(a, b):
    # find the longest common subsequence of a and b
    # if there are multiple LCS, return any one of them
    # if there is no LCS, return an empty list
    pass

def get_smallest_subsequence(a, b):
    # find the smallest subsequence of a and b that is a subsequence of both
    # if there are multiple smallest subsequence, return any one of them
    # if there is no smallest subsequence, return an empty list
    pass

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        subsequence = get_subsequence(a, b)
        if subsequence:
            print("YES")
            print(len(subsequence))
            print(*subsequence)
        else:
            print("NO")

if __name__ == '__main__':
    main()

