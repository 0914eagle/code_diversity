
def solve(strings):
    n = len(strings)
    if n == 1:
        return "YES\n" + strings[0]

    for i in range(n):
        for j in range(i+1, n):
            if strings[i] in strings[j] and not is_substring(strings[i], strings[j]):
                return "NO"

    return "YES\n" + "\n".join(strings)

def is_substring(string1, string2):
    for i in range(len(string2) - len(string1) + 1):
        if string1 == string2[i:i+len(string1)]:
            return True
    return False

