
def solve(numbers):
    return "\n".join(["+91 " + num[4:] if num.startswith(("+91", "91", "0")) else num for num in sorted(numbers)])

