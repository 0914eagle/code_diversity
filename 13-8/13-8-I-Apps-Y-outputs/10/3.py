
def solve(numbers):
    return "\n".join(["+91 " + " ".join(n[-10:][::-1]) for n in numbers])

