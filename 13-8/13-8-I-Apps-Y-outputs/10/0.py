
def solve(numbers):
    return "\n".join(["+91 " + n[4:] if len(n) == 12 and n.startswith("91") else n for n in sorted(numbers)])

