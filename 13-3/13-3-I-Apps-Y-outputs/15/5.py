
def get_available_mb(x, n, months):
    available_mb = x
    for i in range(n):
        available_mb += months[i]
        available_mb -= x
    return available_mb

