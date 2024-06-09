
def get_max_cost(s, p):
    n = len(s)
    count = [0] * 26
    for i in range(n):
        count[ord(s[i]) - ord('a')] += 1
    max_cost = 0
    for i in range(26):
        if count[i] > 0:
            max_cost = max(max_cost, count[i])
    return max_cost

