
def get_available_mb(x, n, p):
    available_mb = x
    for i in range(n):
        available_mb -= p[i]
        if available_mb < 0:
            available_mb = 0
    return available_mb

