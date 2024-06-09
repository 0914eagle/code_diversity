
def is_correct_sequence(sequence):
    stack = []
    for char in sequence:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

def get_min_time(sequence):
    if is_correct_sequence(sequence):
        return 0
    
    n = len(sequence)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            if sequence[j] == "(" and sequence[i - 1] == ")":
                dp[i] = max(dp[i], dp[j] + dp[i - j - 1] + 1)
            elif sequence[j] == ")" and sequence[i - 1] == "(":
                dp[i] = max(dp[i], dp[j] + dp[i - j - 1] + 1)
    
    return dp[n]

def solve(sequence):
    return get_min_time(sequence)

