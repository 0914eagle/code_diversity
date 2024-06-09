
def get_finalists(n, results):
    semifinal_1 = results[:n]
    semifinal_2 = results[n:]
    k = 0
    while k < n:
        if len(set(semifinal_1[:k])) == k and len(set(semifinal_2[:k])) == k:
            break
        k += 1
    finalists = []
    for i in range(n):
        if semifinal_1[i] in set(semifinal_1[:k]) or semifinal_2[i] in set(semifinal_2[:k]):
            finalists.append("1")
        else:
            finalists.append("0")
    return "".join(finalists)

