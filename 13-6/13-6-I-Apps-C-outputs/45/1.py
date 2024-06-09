
def find_triple_correlation(sequence):
    p = len(sequence)
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for n in range(1, p):
                    for m in range(1, p):
                        if (a == b or a == c or b == c) and n == m:
                            continue
                        else:
                            i = 0
                            while i + n + m < p:
                                if sequence[i] == a and sequence[i + n] == b and sequence[i + n + m] == c:
                                    return f"triple correlation {a}({n}){b}({m}){c} found"
                                i += 1
    return "random sequence"

