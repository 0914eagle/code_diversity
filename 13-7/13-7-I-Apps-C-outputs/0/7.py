
import sys
import math

def get_bugs():
    B, T, f = map(int, input().split())
    bugs = []
    for _ in range(B):
        p, s = map(float, input().split())
        bugs.append((p, s))
    return bugs, T, f

def solve(bugs, T, f):
    # Initialize variables
    fix_probs = [bug[0] for bug in bugs]
    severities = [bug[1] for bug in bugs]
    total_severity = 0
    
    # Loop through each hour
    for hour in range(T):
        # Choose the bug with the highest fix probability
        max_prob_idx = fix_probs.index(max(fix_probs))
        
        # Fix the bug with the highest fix probability
        if fix_probs[max_prob_idx] > 0:
            total_severity += severities[max_prob_idx]
            fix_probs[max_prob_idx] = fix_probs[max_prob_idx] * f
        else:
            fix_probs[max_prob_idx] = 0
        
        # Update the fix probabilities
        fix_probs = [prob * f for prob in fix_probs]
    
    return total_severity

def main():
    bugs, T, f = get_bugs()
    print(solve(bugs, T, f))

if __name__ == '__main__':
    main()

