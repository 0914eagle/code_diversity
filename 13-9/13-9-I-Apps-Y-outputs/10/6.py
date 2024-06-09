
def solve_queries(queries):
    result = []
    for query in queries:
        l1, r1, l2, r2 = query
        if l1 == l2:
            result.append([l1, r2])
        elif l1 == r2:
            result.append([l1, l2])
        elif r1 == l2:
            result.append([r1, l2])
        elif r1 == r2:
            result.append([r1, r2])
        else:
            result.append([l1, l2])
    return result

