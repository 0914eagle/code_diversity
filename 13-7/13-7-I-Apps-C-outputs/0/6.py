
import sys
import math

def get_bugs(B, T, f):
    bugs = []
    for _ in range(B):
        p, s = map(float, input().split())
        bugs.append((p, s))
    return bugs

def get_expected_severity(bugs, T, f):
    expected_severity = 0
    for p, s in bugs:
        expected_severity += s * p ** T
    return expected_severity

def get_best_bug_to_fix(bugs, T, f):
    best_bug = None
    best_expected_severity = 0
    for bug in bugs:
        expected_severity = get_expected_severity(bugs, T, f)
        if expected_severity > best_expected_severity:
            best_bug = bug
            best_expected_severity = expected_severity
    return best_bug

def update_bugs(bugs, best_bug, T, f):
    p, s = best_bug
    new_p = p * f ** T
    bugs.remove(best_bug)
    bugs.append((new_p, s))
    return bugs

def main():
    B, T, f = map(int, input().split())
    bugs = get_bugs(B, T, f)
    while T > 0:
        best_bug = get_best_bug_to_fix(bugs, T, f)
        bugs = update_bugs(bugs, best_bug, T, f)
        T -= 1
    print(get_expected_severity(bugs, T, f))

if __name__ == '__main__':
    main()

