
def get_duration(abcd):
    a, b, c, d = map(int, abcd.split())
    return max(0, min(b, d) - max(a, c))

