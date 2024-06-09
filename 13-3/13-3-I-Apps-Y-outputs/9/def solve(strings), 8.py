
def solve(strings):
    n = len(strings)
    if n == 1:
        return "YES\n" + strings[0]

    for i in range(n):
        for j in range(i+1, n):
            if strings[i] in strings[j] and not strings[j] in strings[i]:
                return "NO"

    return "YES\n" + "\n".join(strings)

