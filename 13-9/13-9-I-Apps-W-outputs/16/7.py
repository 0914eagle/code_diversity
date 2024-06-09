
def get_occurrences(s, p):
    occurrences = 0
    for i in range(len(s)):
        if s[i:i+len(p)] == p:
            occurrences += 1
    return occurrences

def solve(s, p):
    max_occurrences = []
    for x in range(len(s)+1):
        s_prime = s[:x] + s[x+len(p):]
        occurrences = get_occurrences(s_prime, p)
        max_occurrences.append(occurrences)
    return max_occurrences

