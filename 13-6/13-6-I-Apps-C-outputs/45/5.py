
def find_triple_correlation(sequence):
    p = len(sequence)
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for n in range(1, p):
                    for m in range(1, p):
                        if (a == b or b == c or c == a) and n == m:
                            continue
                        count = 0
                        for i in range(p):
                            if sequence[i] == a:
                                for j in range(i+n, min(i+n+m, p)):
                                    if sequence[j] == b:
                                        for k in range(j+m, min(j+m+n, p)):
                                            if sequence[k] == c:
                                                count += 1
                                                break
                                        if count == 0:
                                            break
                                    else:
                                        break
                                if count == 0:
                                    break
                            elif sequence[i] == b:
                                for j in range(i+m, min(i+m+n, p)):
                                    if sequence[j] == c:
                                        for k in range(j+n, min(j+n+m, p)):
                                            if sequence[k] == a:
                                                count += 1
                                                break
                                        if count == 0:
                                            break
                                    else:
                                        break
                                if count == 0:
                                    break
                            elif sequence[i] == c:
                                for j in range(i+n+m, min(i+n+m+n, p)):
                                    if sequence[j] == b:
                                        count += 1
                                        break
                                if count == 0:
                                    break
                        if count >= ceil(p/40) + 1:
                            return f"triple correlation {a}({n}){b}({m}){c} found"
    return "random sequence"

