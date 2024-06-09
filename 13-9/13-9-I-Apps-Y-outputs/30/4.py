
def solve(numbers):
    return "\n".join(sorted(numbers, key=lambda x: x.strip("+91").strip("91").strip("0")))

