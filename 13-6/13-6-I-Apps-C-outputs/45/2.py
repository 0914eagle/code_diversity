
def find_triple_correlation(sequence):
    p = len(sequence)
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for n in range(1, p):
                    for m in range(1, p):
                        if (a == b or a == c or b == c) and n == m:
                            continue
                        count = 0
                        for i in range(p - n - m):
                            if sequence[i] == a and sequence[i + n] == b and sequence[i + n + m] == c:
                                count += 1
                        if count >= ceil(p / 40) + 1:
                            return f"triple correlation {a}({n}){b}({m}){c} found"
    return "random sequence"

