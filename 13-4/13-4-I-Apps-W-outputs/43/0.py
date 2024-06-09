
def solve(names):
    seen = set()
    result = []
    for name in names:
        if name in seen:
            result.append("YES")
        else:
            result.append("NO")
            seen.add(name)
    return result

