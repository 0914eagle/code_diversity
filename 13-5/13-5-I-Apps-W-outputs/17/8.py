
import sys

def solve(n, m, p, subsequence):
    # Initialize the answer
    answer = 0

    # Iterate over all possible strings of length n
    for i in range(1, n + 1):
        # Create a string of length n
        s = "z" * i

        # Check if the string matches the given subsequence
        if s[subsequence[0] - 1] == p[0] and s[subsequence[-1] - 1] == p[-1]:
            # Check if the string is a valid substring
            if all(s[subsequence[j] - 1] == p[j] for j in range(m)):
                answer += 1

    # Return the answer modulo 10^9 + 7
    return answer % 1000000007

if __name__ == "__main__":
    n, m = map(int, input().split())
    p = input()
    subsequence = list(map(int, input().split()))
    print(solve(n, m, p, subsequence))

