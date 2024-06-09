
def check_error(t):
    if len(t) < 2:
        return "NO"
    for i in range(len(t) - 1):
        if t[i] == t[i+1]:
            return "YES\n" + t[i]
    return "NO"

