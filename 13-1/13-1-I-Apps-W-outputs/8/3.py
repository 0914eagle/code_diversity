
def solve(w, m, k):
    max_length = 0
    for i in range(m, w+1):
        length = 1
        while i > 0:
            length += 1
            i //= 10
        if length * k <= w:
            max_length = max(max_length, length)
    return max_length

