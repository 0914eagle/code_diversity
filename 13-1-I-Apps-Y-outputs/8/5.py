
def solve(s):
    n = len(s)
    count_a = s.count("a")
    count_b = s.count("b")
    if count_a > count_b:
        return "a" * (n // 2) + "b" * (n // 2)
    elif count_b > count_a:
        return "b" * (n // 2) + "a" * (n // 2)
    else:
        return s

