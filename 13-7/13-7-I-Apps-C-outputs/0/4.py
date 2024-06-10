
import sys

def get_input():
    B, T, f = map(int, input().split())
    bugs = []
    for _ in range(B):
        p, s = map(float, input().split())
        bugs.append((p, s))
    return B, T, f, bugs

def get_expected_severity(bugs, f):
    expected_severity = 0
    for p, s in bugs:
        expected_severity += p * s
    return expected_severity

def get_new_bugs(bugs, f):
    new_bugs = []
    for p, s in bugs:
        new_p = p * f
        new_bugs.append((new_p, s))
    return new_bugs

def solve(B, T, f, bugs):
    expected_severity = 0
    for t in range(T):
        expected_severity += get_expected_severity(bugs, f)
        bugs = get_new_bugs(bugs, f)
    return expected_severity

if __name__ == '__main__':
    B, T, f, bugs = get_input()
    print(solve(B, T, f, bugs))

