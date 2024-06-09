
def solve(numbers):
    return "\n".join(["+91 " + " ".join(n[4:6] + n[7:9] + n[10:12]) for n in sorted(numbers)])

