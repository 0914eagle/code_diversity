
def solve_queries(queries):
    answers = []
    for query in queries:
        l1, r1, l2, r2 = query
        if l1 <= l2:
            a = l1
            b = l2
        else:
            a = l2
            b = l1
        answers.append([a, b])
    return answers

