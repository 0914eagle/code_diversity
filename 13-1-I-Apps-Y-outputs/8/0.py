
def solve(s):
    n = len(s)
    count_a = s.count("a")
    count_b = s.count("b")
    if count_a > count_b:
        return "impossible"
    else:
        return n - count_a

