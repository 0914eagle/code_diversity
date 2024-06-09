
def solve_queries(queries):
    answers = []
    for query in queries:
        l1, r1, l2, r2 = map(int, query)
        a = max(l1, l2)
        b = min(r1, r2)
        if a < b:
            answers.append([a, b])
        else:
            answers.append([b, a])
    return answers

