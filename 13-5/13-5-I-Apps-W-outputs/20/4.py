
def get_max_value(A, B, N):
    max_value = 0
    for x in range(N+1):
        value = floor(A*x/B) - A*floor(x/B)
        if value > max_value:
            max_value = value
    return max_value

