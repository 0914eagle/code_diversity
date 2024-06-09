
def get_available_mb(x, n, p_list):
    available_mb = x
    for i in range(n):
        available_mb += p_list[i]
        available_mb -= min(p_list[i], available_mb)
    return available_mb

