
def solve(s):
    n = len(s)
    prefixes = []
    suffixes = []
    for i in range(1, n):
        prefixes.append(s[:i])
        suffixes.append(s[i:])
    prefixes = list(set(prefixes))
    suffixes = list(set(suffixes))
    result = ""
    for i in range(len(prefixes)):
        if prefixes[i] in suffixes:
            result += "S"
            suffixes.remove(prefixes[i])
        else:
            result += "P"
    return result

