
def solve(strings, operations):
    for a, b in operations:
        strings[a-1] += strings[b-1]
        strings[b-1] = ""
    return strings[-1]

