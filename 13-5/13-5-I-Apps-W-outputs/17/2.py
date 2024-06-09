
import sys

def solve(n, m, p, subsequence):
    # Initialize the answer
    answer = 0

    # Iterate over all possible strings of length n
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Check if the current string matches the given subsequence
            if subsequence[0] == i and subsequence[-1] == j:
                # Check if the current string matches the given pattern
                if "".join(sorted(p)) == "".join(sorted(s[i:j])):
                    answer += 1

    # Return the answer modulo 10^9 + 7
    return answer % 1000000007

if __name__ == '__main__':
    n, m = map(int, input().split())
    p = input()
    subsequence = list(map(int, input().split()))
    print(solve(n, m, p, subsequence))

