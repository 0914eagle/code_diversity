
import sys

def get_bug_info():
    B, T, f = map(int, input().split())
    bugs = []
    for _ in range(B):
        p, s = map(float, input().split())
        bugs.append((p, s))
    return B, T, f, bugs

def solve(B, T, f, bugs):
    # Initialize variables
    fixed_bugs = []
    unfixed_bugs = bugs
    total_severity = 0
    
    # Loop through each hour
    for hour in range(T):
        # Choose the bug with the highest probability of being fixed
        bug_to_fix = max(unfixed_bugs, key=lambda x: x[0])
        
        # Fix the bug with probability p
        if bug_to_fix[0] >= 1:
            fixed_bugs.append(bug_to_fix)
            unfixed_bugs.remove(bug_to_fix)
            total_severity += bug_to_fix[1]
        else:
            # Reduce the probability of fixing the bug if it fails
            bug_to_fix = (bug_to_fix[0] * f, bug_to_fix[1])
            unfixed_bugs.remove(bug_to_fix)
            unfixed_bugs.append(bug_to_fix)
    
    return total_severity

def main():
    B, T, f, bugs = get_bug_info()
    print(solve(B, T, f, bugs))

if __name__ == '__main__':
    main()

