
def solve(numbers):
    return "\n".join(["+91 " + " ".join(n[-10:-5]) + " " + " ".join(n[-5:]) for n in sorted(numbers)])

