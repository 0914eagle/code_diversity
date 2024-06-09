
def find_triple_correlation(sequence):
    p = len(sequence)
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for n in range(1, 10):
                    for m in range(1, 10):
                        if (a == b or b == c or c == a) and n == m == 1:
                            continue
                        if check_triple_correlation(sequence, a, b, c, n, m, p):
                            return f"triple correlation {a}({n}){b}({m}){c} found"
    return "random sequence"

def check_triple_correlation(sequence, a, b, c, n, m, p):
    count = 0
    for i in range(p - n - m):
        if sequence[i] == a and sequence[i + n] == b and sequence[i + n + m] == c:
            count += 1
        if sequence[i] == b and sequence[i + m] == c and sequence[i + n] == a:
            count += 1
        if sequence[i] == a and sequence[i + n + m] == b and sequence[i + n] == c:
            count += 1
        if count >= ceil(p / 40) + 1:
            return True
    return False

def ceil(x):
    return -int(x) if x < 0 else int(x + 0.999999)

