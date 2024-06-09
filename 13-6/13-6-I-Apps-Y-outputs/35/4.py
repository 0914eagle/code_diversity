
def solve(s):
    n = len(s)
    prefixes = []
    suffixes = []
    for i in range(1, n):
        prefixes.append(s[:i])
        suffixes.append(s[i:])
    prefixes = list(set(prefixes))
    suffixes = list(set(suffixes))
    answer = []
    for i in range(len(prefixes)):
        if prefixes[i] in suffixes:
            answer.append('P')
            suffixes.remove(prefixes[i])
        else:
            answer.append('S')
    return ''.join(answer)

