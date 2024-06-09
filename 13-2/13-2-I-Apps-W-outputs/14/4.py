
def f1(s, a, b):
    if len(s) < a or len(s) < b:
        return "NO"
    if a % b == 0:
        return "YES"
    return "NO"

